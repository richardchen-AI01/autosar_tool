package cn.com.myorg.mal.admindata;

import autosar40.autosartoplevelstructure.AUTOSAR;
import autosar40.genericstructure.generaltemplateclasses.admindata.AdminData;
import autosar40.genericstructure.generaltemplateclasses.arobject.ARObject;
import autosar40.genericstructure.generaltemplateclasses.identifiable.Identifiable;
import autosar40.genericstructure.generaltemplateclasses.specialdata.Sd;
import autosar40.genericstructure.generaltemplateclasses.specialdata.Sdg;
import autosar40.genericstructure.generaltemplateclasses.specialdata.SdgContents;
import autosar40.util.Autosar40Factory;
import java.util.List;
import org.eclipse.emf.transaction.RecordingCommand;
import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sphinx.emf.util.WorkspaceEditingDomainUtil;

/**
 * 99% paraphrase of cn.com.isoft.mal.admindata.ArccoreOption (208 lines).
 * Only divergence (1% allowed): write path uses RecordingCommand on
 * TransactionalEditingDomain.getCommandStack() instead of reference's
 * TransactionUtils.executeQueue — equivalent EMF transactional write,
 * branch structure preserved.
 */
public abstract class ArccoreOption {
    public static final String OPT_LOCAL_VALIDATE = "LOCAL_VALIDATION";
    public static final String OPT_LOCAL_DECORATE = "LOCAL_DECORATION";
    public static final String OPT_GENERATORDIR = "GENDIR";
    public static final String OPT_AUTHOR = "AUTHOR";
    public static final String OPT_COPYRIGHT = "COPYRIGHT";
    public static final String OFF = "OFF";
    public static final String ON = "ON";

    private ARObject owner;
    private Sdg sdg_internal;
    private Autosar40Factory factory = Autosar40Factory.eINSTANCE;

    public ArccoreOption(AUTOSAR autosar) {
        this.owner = autosar;
    }

    public ArccoreOption(Identifiable identifiable) {
        this.owner = identifiable;
    }

    private AdminData getAdminData() {
        if (this.owner instanceof Identifiable) {
            return ((Identifiable) this.owner).getAdminData();
        }
        return ((AUTOSAR) this.owner).getAdminData();
    }

    private void setAdminData(AdminData aD) {
        if (this.owner instanceof Identifiable) {
            ((Identifiable) this.owner).setAdminData(aD);
        } else {
            ((AUTOSAR) this.owner).setAdminData(aD);
        }
    }

    private String getName() {
        if (this.owner instanceof Identifiable) {
            return ((Identifiable) this.owner).getShortName();
        }
        return this.owner.eResource().toString();
    }

    private Sdg getSdgInternal() {
        if (this.sdg_internal != null) {
            return this.sdg_internal;
        }
        Sdg sdg = null;
        try {
            for (Sdg s : this.getAdminData().getSdgs()) {
                if (!s.getGid().equals(this.getSdgId())) continue;
                sdg = s;
                break;
            }
        } catch (NullPointerException nullPointerException) {
            // empty catch block (跟反编一致)
        }
        if (sdg != null) {
            this.sdg_internal = sdg;
        }
        return sdg;
    }

    private Runnable create() {
        SdgContents sdgContents;
        boolean update = false;
        AdminData adminData = this.getAdminData();
        if (adminData == null) {
            adminData = this.factory.createAdminData();
            update = true;
        }
        Sdg sdg = null;
        for (Sdg s : adminData.getSdgs()) {
            if (!s.getGid().equals(this.getSdgId())) continue;
            sdg = s;
            break;
        }
        if (sdg == null) {
            sdg = this.factory.createSdg();
            sdg.setGid(this.getSdgId());
            update = true;
        }
        if ((sdgContents = sdg.getSdgContentsType()) == null) {
            sdgContents = this.factory.createSdgContents();
            update = true;
        }
        final AdminData aD = adminData;
        final Sdg s = sdg;
        final SdgContents sdgC = sdgContents;
        if (update) {
            return new Runnable() {
                @Override
                public void run() {
                    ArccoreOption.this.setAdminData(aD);
                    if (!ArccoreOption.this.getAdminData().getSdgs().contains(s)) {
                        ArccoreOption.this.getAdminData().getSdgs().add(s);
                    }
                    s.setSdgContentsType(sdgC);
                }
            };
        }
        return null;
    }

    private void updateModel(final Runnable runnable) {
        TransactionalEditingDomain domain = WorkspaceEditingDomainUtil.getEditingDomain(this.owner);
        if (domain != null) {
            domain.getCommandStack().execute(new RecordingCommand(domain, "ArccoreOption updateModel") {
                @Override
                protected void doExecute() {
                    runnable.run();
                }
            });
        } else {
            runnable.run();
        }
    }

    public abstract String getSdgId();

    public void setOption(final String option, String value) {
        this.checkOptionState();
        TransactionalEditingDomain domain = WorkspaceEditingDomainUtil.getEditingDomain(this.getSdgInternal());
        final Sd sd = this.factory.createSd();
        sd.setGid(option);
        sd.setValue(value);
        if (domain != null) {
            final Runnable createRunnable = this.create();
            domain.getCommandStack().execute(new RecordingCommand(domain,
                    "Set option " + option + " for " + this.getName() + " to " + value) {
                @Override
                protected void doExecute() {
                    if (createRunnable != null) {
                        createRunnable.run();
                    }
                    ArccoreOption.this.getSdgInternal().getSdgContentsType().getSds()
                            .remove(ArccoreOption.this.getOptionSd(option));
                    ArccoreOption.this.getSdgInternal().getSdgContentsType().getSds().add(sd);
                }
            });
        } else {
            this.getSdgInternal().getSdgContentsType().getSds().remove(this.getOptionSd(option));
            this.getSdgInternal().getSdgContentsType().getSds().add(sd);
        }
    }

    public String getOption(String option) {
        Sd sd = null;
        if (this.getSdgInternal() != null && this.getSdgInternal().getSdgContentsType() != null) {
            for (Sd s : this.getSdgInternal().getSdgContentsType().getSds()) {
                if (!s.getGid().equals(option)) continue;
                sd = s;
                break;
            }
        }
        if (sd != null) {
            return sd.getValue();
        }
        return "";
    }

    public Sd getOptionSd(String option) {
        this.checkOptionState();
        for (Sd sd : this.getSdgInternal().getSdgContentsType().getSds()) {
            if (!sd.getGid().equals(option)) continue;
            return sd;
        }
        return null;
    }

    public void addIfNotPresent() {
        this.checkOptionState();
    }

    private void checkOptionState() {
        Runnable r = this.create();
        if (r != null) {
            this.updateModel(r);
        }
    }

    public Sdg getSdg() {
        return this.getSdgInternal();
    }
}
