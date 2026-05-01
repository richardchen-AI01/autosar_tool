package cn.com.myorg.bswbuilder.ui.schema;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

/**
 * Parses an ECUC parameter definition file ({@code <Module>Def.arxml}) into
 * a {@link ModuleSchema} tree. Drives all generic FormPages (E5-2/3/4).
 *
 * <p>Implementation: plain {@code javax.xml.parsers} DOM walk. We deliberately
 * avoid ARTOP / Sphinx EMF — those bring 30+MB of metamodel jars + transactional
 * editing domain machinery we don't need just to render widget forms. The
 * XPath-equivalent pattern is straightforward (every ECUC-*-PARAM-DEF element
 * is uniquely identified by its tag name + child SHORT-NAME).
 *
 * <p>Reference: V25.10's {@code GModuleConfiguration.gGetDefinition() →
 * GModuleDef.gGetContainers()} produces the equivalent tree via EMF; we get
 * there by DOM. Outputs are interchangeable for {@code GenericGeneralFormPage}
 * / {@code GenericMasterDetailFormPage} consumption.
 */
public final class BswmdSchemaReader {

    private BswmdSchemaReader() {}

    public static ModuleSchema parse(File defArxml) throws IOException {
        try {
            DocumentBuilder b = DocumentBuilderFactory.newInstance().newDocumentBuilder();
            Document doc = b.parse(defArxml);
            return parseRoot(doc);
        } catch (ParserConfigurationException | SAXException e) {
            throw new IOException("Failed to parse " + defArxml + ": " + e.getMessage(), e);
        }
    }

    public static ModuleSchema parse(InputStream in, String sourceLabel) throws IOException {
        try {
            DocumentBuilder b = DocumentBuilderFactory.newInstance().newDocumentBuilder();
            Document doc = b.parse(in);
            return parseRoot(doc);
        } catch (ParserConfigurationException | SAXException e) {
            throw new IOException("Failed to parse " + sourceLabel + ": " + e.getMessage(), e);
        }
    }

    // ============================================================ DOM parse

    private static ModuleSchema parseRoot(Document doc) {
        // ECUC-MODULE-DEF lives at the leaf of nested AR-PACKAGE / ELEMENTS.
        // Walk all descendants; first ECUC-MODULE-DEF wins (typical shape: 1 per
        // module-def file).
        Element moduleDef = firstByTag(doc.getDocumentElement(), "ECUC-MODULE-DEF");
        if (moduleDef == null) {
            return new ModuleSchema("", null, new ArrayList<ContainerSchema>());
        }
        String name = childText(moduleDef, "SHORT-NAME");
        String desc = descL2(moduleDef);

        List<ContainerSchema> containers = new ArrayList<>();
        Element containersElem = firstChildByTag(moduleDef, "CONTAINERS");
        if (containersElem != null) {
            for (Element cdef : childElements(containersElem)) {
                ContainerSchema cs = parseContainer(cdef);
                if (cs != null) containers.add(cs);
            }
        }
        return new ModuleSchema(name, desc, containers);
    }

    private static ContainerSchema parseContainer(Element cdef) {
        String tag = cdef.getTagName();
        boolean choice;
        if ("ECUC-PARAM-CONF-CONTAINER-DEF".equals(tag)) {
            choice = false;
        } else if ("ECUC-CHOICE-CONTAINER-DEF".equals(tag)) {
            choice = true;
        } else {
            return null;
        }
        String name = childText(cdef, "SHORT-NAME");
        String desc = descL2(cdef);
        long lower = parseLong(childText(cdef, "LOWER-MULTIPLICITY"), 1);
        long upper = parseUpper(childText(cdef, "UPPER-MULTIPLICITY"));
        boolean generalFlag = readGeneralFlag(cdef);

        List<ParamSchema> params = new ArrayList<>();
        Element parameters = firstChildByTag(cdef, "PARAMETERS");
        if (parameters != null) {
            for (Element p : childElements(parameters)) {
                ParamSchema ps = parseParam(p);
                if (ps != null) params.add(ps);
            }
        }

        // References (ECUC-REFERENCE-DEF / ECUC-FOREIGN-REFERENCE-DEF /
        // ECUC-CHOICE-REFERENCE-DEF) treated as ParamSchema entries with
        // type=REFERENCE / FOREIGN_REFERENCE / CHOICE_REFERENCE — surface to the
        // form as a "browse and pick" widget. Lives next to PARAMETERS in
        // REFERENCES element.
        Element references = firstChildByTag(cdef, "REFERENCES");
        if (references != null) {
            for (Element r : childElements(references)) {
                ParamSchema ref = parseReference(r);
                if (ref != null) params.add(ref);
            }
        }

        // Recurse into SUB-CONTAINERS (or CHOICES for ECUC-CHOICE-CONTAINER-DEF).
        List<ContainerSchema> subs = new ArrayList<>();
        Element sub = firstChildByTag(cdef, "SUB-CONTAINERS");
        if (sub == null) sub = firstChildByTag(cdef, "CHOICES");
        if (sub != null) {
            for (Element scdef : childElements(sub)) {
                ContainerSchema scs = parseContainer(scdef);
                if (scs != null) subs.add(scs);
            }
        }
        return new ContainerSchema(name, desc, lower, upper, generalFlag, choice, params, subs);
    }

    private static ParamSchema parseParam(Element p) {
        String tag = p.getTagName();
        ParamType type;
        switch (tag) {
            case "ECUC-BOOLEAN-PARAM-DEF":     type = ParamType.BOOLEAN;     break;
            case "ECUC-INTEGER-PARAM-DEF":     type = ParamType.INTEGER;     break;
            case "ECUC-FLOAT-PARAM-DEF":       type = ParamType.FLOAT;       break;
            case "ECUC-STRING-PARAM-DEF":      type = ParamType.STRING;      break;
            case "ECUC-ENUMERATION-PARAM-DEF": type = ParamType.ENUMERATION; break;
            default:
                return null;  // Reference defs are handled in parseReference()
        }
        String name = childText(p, "SHORT-NAME");
        String desc = descL2(p);
        String def  = childText(p, "DEFAULT-VALUE");
        long lower  = parseLong(childText(p, "LOWER-MULTIPLICITY"), 1);
        long upper  = parseUpper(childText(p, "UPPER-MULTIPLICITY"));
        String min  = childText(p, "MIN");
        String max  = childText(p, "MAX");

        List<String> literals = new ArrayList<>();
        if (type == ParamType.ENUMERATION) {
            Element lits = firstChildByTag(p, "LITERALS");
            if (lits != null) {
                for (Element l : childElementsByTag(lits, "ECUC-ENUMERATION-LITERAL-DEF")) {
                    String lname = childText(l, "SHORT-NAME");
                    if (lname != null) literals.add(lname);
                }
            }
        }
        return new ParamSchema(name, type, desc, def, lower, upper, min, max, literals, null);
    }

    private static ParamSchema parseReference(Element r) {
        String tag = r.getTagName();
        ParamType type;
        switch (tag) {
            case "ECUC-REFERENCE-DEF":         type = ParamType.REFERENCE;         break;
            case "ECUC-FOREIGN-REFERENCE-DEF": type = ParamType.FOREIGN_REFERENCE; break;
            case "ECUC-CHOICE-REFERENCE-DEF":  type = ParamType.CHOICE_REFERENCE;  break;
            default:
                return null;
        }
        String name  = childText(r, "SHORT-NAME");
        String desc  = descL2(r);
        long lower   = parseLong(childText(r, "LOWER-MULTIPLICITY"), 1);
        long upper   = parseUpper(childText(r, "UPPER-MULTIPLICITY"));

        // Destination: DESTINATION-REF (ECUC-REFERENCE-DEF / ECUC-FOREIGN-REFERENCE-DEF)
        // or DESTINATION-TYPE for FOREIGN. Just take the text content; consumers
        // need only the path string for the chooser dialog.
        String dest = childText(r, "DESTINATION-REF");
        if (dest == null) dest = childText(r, "DESTINATION-TYPE");

        return new ParamSchema(name, type, desc, null, lower, upper, null, null,
                new ArrayList<String>(), dest);
    }

    /**
     * Reads {@code <ADMIN-DATA><SDGS><SDG GID="iSoft::IdentifiableOptions">
     *     <SD GID="GENERAL_FLAG">true</SD></SDG></SDGS></ADMIN-DATA>}.
     * Reference uses GENERAL_FLAG to signal "this container is a single-instance
     * 'General' tab" (跟 BswModuleGeneralFormPage 派发逻辑一致).
     */
    private static boolean readGeneralFlag(Element container) {
        Element adminData = firstChildByTag(container, "ADMIN-DATA");
        if (adminData == null) return false;
        Element sdgs = firstChildByTag(adminData, "SDGS");
        if (sdgs == null) return false;
        for (Element sdg : childElementsByTag(sdgs, "SDG")) {
            for (Element sd : childElementsByTag(sdg, "SD")) {
                if ("GENERAL_FLAG".equals(sd.getAttribute("GID"))
                        && "true".equalsIgnoreCase(textOf(sd))) {
                    return true;
                }
            }
        }
        return false;
    }

    // ============================================================ DOM helpers

    private static String childText(Element parent, String tag) {
        Element c = firstChildByTag(parent, tag);
        return c == null ? null : textOf(c);
    }

    private static String descL2(Element parent) {
        Element desc = firstChildByTag(parent, "DESC");
        if (desc == null) return null;
        Element l2 = firstChildByTag(desc, "L-2");
        return l2 == null ? null : textOf(l2);
    }

    private static Element firstChildByTag(Element parent, String tag) {
        NodeList kids = parent.getChildNodes();
        for (int i = 0; i < kids.getLength(); i++) {
            Node n = kids.item(i);
            if (n.getNodeType() == Node.ELEMENT_NODE && tag.equals(((Element) n).getTagName())) {
                return (Element) n;
            }
        }
        return null;
    }

    private static Element firstByTag(Element root, String tag) {
        if (tag.equals(root.getTagName())) return root;
        NodeList desc = root.getElementsByTagName(tag);
        return desc.getLength() == 0 ? null : (Element) desc.item(0);
    }

    private static List<Element> childElements(Element parent) {
        List<Element> out = new ArrayList<>();
        NodeList kids = parent.getChildNodes();
        for (int i = 0; i < kids.getLength(); i++) {
            Node n = kids.item(i);
            if (n.getNodeType() == Node.ELEMENT_NODE) out.add((Element) n);
        }
        return out;
    }

    private static List<Element> childElementsByTag(Element parent, String tag) {
        List<Element> out = new ArrayList<>();
        NodeList kids = parent.getChildNodes();
        for (int i = 0; i < kids.getLength(); i++) {
            Node n = kids.item(i);
            if (n.getNodeType() == Node.ELEMENT_NODE
                    && tag.equals(((Element) n).getTagName())) {
                out.add((Element) n);
            }
        }
        return out;
    }

    private static String textOf(Element e) {
        if (e == null) return null;
        String t = e.getTextContent();
        return t == null ? null : t.trim();
    }

    private static long parseLong(String s, long fallback) {
        if (s == null) return fallback;
        try { return Long.parseLong(s.trim()); } catch (NumberFormatException nfe) { return fallback; }
    }

    /** "*" → -1 (unbounded); else parsed as long; missing → 1. */
    private static long parseUpper(String s) {
        if (s == null) return 1;
        s = s.trim();
        return "*".equals(s) ? -1 : parseLong(s, 1);
    }
}
