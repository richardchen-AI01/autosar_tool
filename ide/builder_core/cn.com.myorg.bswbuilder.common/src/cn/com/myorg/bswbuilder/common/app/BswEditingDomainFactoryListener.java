package cn.com.myorg.bswbuilder.common.app;

import org.eclipse.emf.transaction.TransactionalEditingDomain;
import org.eclipse.sphinx.emf.domain.factory.ITransactionalEditingDomainFactoryListener;

/**
 * No-op listener for Sphinx's editing domain factory. The mere act of
 * registering this listener (via the {@code editingDomainFactoryListeners}
 * extension point with an {@code applicableFor} metamodel pattern) tells
 * Sphinx "AUTOSAR metamodel resources should have a TransactionalEditingDomain
 * created for them" — without this registration, Sphinx's
 * {@code ModelDescriptor.getLoadedResources()} calls
 * {@code TransactionUtil.runExclusive(domain, …)} with {@code domain == null},
 * triggering the NPE that pops up after every Generate / file change.
 *
 * <p>iSoft's reference V25.10 has a much fancier listener
 * ({@code cn.com.isoft.pal.listeners.TransactionalEditingDomainFactoryListener})
 * that installs a custom {@code ResourceSetListenerImpl} on each created
 * domain to track resource set changes — useful for their workspace-wide
 * sync features. v0.1 doesn't need that tracking; an empty hook is enough
 * to fix the NPE root cause (no domain registered for the metamodel).
 */
public class BswEditingDomainFactoryListener
        implements ITransactionalEditingDomainFactoryListener {

    @Override
    public void postCreateEditingDomain(TransactionalEditingDomain domain) {
        // No-op. Reference V25.10 installs a custom ResourceSetListener here
        // for cross-resource sync; v0.1 doesn't need it.
    }

    @Override
    public void preDisposeEditingDomain(TransactionalEditingDomain domain) {
        // No-op.
    }
}
