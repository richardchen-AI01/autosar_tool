package cn.com.myorg.bswbuilder.ui.editors;

import java.io.File;

import org.eclipse.core.runtime.IProgressMonitor;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.widgets.Display;
import org.eclipse.ui.IEditorInput;
import org.eclipse.ui.IEditorSite;
import org.eclipse.ui.IPathEditorInput;
import org.eclipse.ui.PartInitException;
import org.eclipse.ui.forms.editor.FormEditor;

import cn.com.myorg.bswbuilder.modules.memif.data.MemIfArxmlReader;
import cn.com.myorg.bswbuilder.modules.memif.data.MemIfData;
import cn.com.myorg.bswbuilder.ui.editors.pages.MemIfGeneralFormPage;

/**
 * Multi-page form editor for a MemIf ARXML — center pane in the EB-tresos
 * style perspective, mirrors iSoft V25.10's
 * {@code cn.com.isoft.bswbuilder.ui.editor.NewBswBuilderEditor} but built
 * directly on Eclipse {@code FormEditor}, skipping iSoft's pal middle
 * layer (per docs/reference/decompiled-memif/isoft-impl-notes.md §2).
 *
 * <p>v0.1: one page — {@link MemIfGeneralFormPage} —
 * containing MemIfGeneral / MemIfPublishedInformation. v0.2 will add
 * one page per top-level container.
 *
 * <p>Dirty tracking + Save flow:
 * the page reports dirty state via {@link #setDirty(boolean)};
 * {@link #doSave(IProgressMonitor)} delegates to the page's
 * {@code commit(boolean)} which writes via
 * {@code MemIfArxmlWriter} (string-surgery, byte-equal preserving).
 */
public class MemIfModuleManagerEditor extends FormEditor {

    public static final String ID =
            "cn.com.myorg.bswbuilder.ui.editors.MemIfModuleManagerEditor";

    private File arxmlFile;
    private MemIfData loadedData;
    private MemIfGeneralFormPage generalPage;
    private boolean dirty;

    @Override
    public void init(IEditorSite site, IEditorInput input) throws PartInitException {
        File f = resolveFile(input);
        if (f == null) {
            throw new PartInitException(
                    "Unsupported editor input: " + input.getClass().getName());
        }
        if (!f.isFile()) {
            throw new PartInitException("ARXML file not found: " + f.getAbsolutePath());
        }
        this.arxmlFile = f;

        try {
            this.loadedData = MemIfArxmlReader.read(f.getAbsolutePath());
        } catch (Throwable t) {
            throw new PartInitException("Failed to load ARXML: " + t.getMessage(), t);
        }

        super.init(site, input);
        setPartName(f.getName());
    }

    private static File resolveFile(IEditorInput input) {
        // v0.1: only IPathEditorInput. Autosar Explorer always opens via
        // LocalFileEditorInput which is IPathEditorInput. IFileEditorInput
        // would need org.eclipse.ui.ide bundle — defer to v0.2 if a workspace-
        // backed flow is added.
        if (input instanceof IPathEditorInput) {
            return ((IPathEditorInput) input).getPath().toFile();
        }
        return null;
    }

    @Override
    protected void addPages() {
        try {
            generalPage = new MemIfGeneralFormPage(this, loadedData);
            addPage(generalPage);
        } catch (PartInitException e) {
            e.printStackTrace();
        }
    }

    /** Called by the page when widgets change. */
    public void setDirty(boolean d) {
        if (this.dirty == d) return;
        this.dirty = d;
        Display.getDefault().asyncExec(new Runnable() {
            @Override public void run() { firePropertyChange(PROP_DIRTY); }
        });
    }

    @Override public boolean isDirty() { return dirty; }
    @Override public boolean isSaveAsAllowed() { return false; }

    @Override
    public void doSave(IProgressMonitor monitor) {
        if (generalPage == null) return;
        try {
            int wrote = generalPage.commit();
            if (wrote >= 0) {
                // Reload from disk so the form reflects what's actually saved
                loadedData = MemIfArxmlReader.read(arxmlFile.getAbsolutePath());
                generalPage.reload(loadedData);
                setDirty(false);
            }
        } catch (Throwable t) {
            t.printStackTrace();
            MessageDialog.openError(getSite().getShell(),
                    "Save failed",
                    t.getClass().getSimpleName() + ": " + t.getMessage());
        }
    }

    @Override
    public void doSaveAs() {
        // Save As not supported for ARXML in v0.1
    }

    public File getArxmlFile() { return arxmlFile; }
    public MemIfData getLoadedData() { return loadedData; }
}
