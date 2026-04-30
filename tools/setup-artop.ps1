# tools/setup-artop.ps1 — copy Artop AAL + Eclipse Sphinx jars from a local
# ORIENTAIS_Studio install into ide/target-platform/bswbuilder-target/local-plugins/
# so Tycho's Directory location can resolve them.
#
# Run on Win, from anywhere:
#   pwsh tools/setup-artop.ps1
#   pwsh tools/setup-artop.ps1 -OrientaisRoot 'D:\ORIENTAIS_Studio\ORIENTAIS_Configurator_for_EasyXMen_V25.10'
#
# Without ORIENTAIS access, IDE bundles that don't Require-Bundle Artop/Sphinx
# (common, ui, modules.memif at v0.1) still build. Phase 1+ work that imports
# Artop classes needs this script to have run.

[CmdletBinding()]
param(
    [string]$OrientaisRoot = 'D:\ORIENTAIS_Studio\ORIENTAIS_Configurator_for_EasyXMen_V25.10'
)

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Src = Join-Path $OrientaisRoot 'plugins'
# Tycho's Directory target-platform location expects the standard Eclipse
# install layout: <root>/plugins/*.jar and optionally <root>/features/*.jar.
# Flat <root>/*.jar is silently ignored.
$Dst = Join-Path $RepoRoot 'ide/target-platform/bswbuilder-target/local-plugins/plugins'

if (-not (Test-Path $Src)) {
    Write-Error "ORIENTAIS plugins dir not found: $Src"
    exit 1
}

if (-not (Test-Path $Dst)) {
    New-Item -ItemType Directory -Path $Dst -Force | Out-Null
}

# Patterns to copy:
# - org.artop.* — AUTOSAR Artop AAL
# - org.eclipse.sphinx.* — Sphinx (EMF + workspace integration)
# - com.google.inject — Guice; transitively required by org.artop.aal.gautosar.services
#                      (Eclipse 2018-12 p2 doesn't ship guice; it lives in
#                      ORIENTAIS plugins dir alongside Artop)
$patterns = @('org.artop.*.jar', 'org.eclipse.sphinx.*.jar', 'com.google.inject*.jar')
$copied = 0
$bytes = 0

foreach ($pat in $patterns) {
    Get-ChildItem -Path $Src -Filter $pat | ForEach-Object {
        Copy-Item $_.FullName -Destination $Dst -Force
        $copied++
        $bytes += $_.Length
    }
}

Write-Host ("[setup-artop] copied {0} jars ({1:N1} MB) into {2}" -f $copied, ($bytes / 1MB), $Dst)
