# Updater

Package `FNS_Updater`.

In-place toolkit updates, with settings preserved across the replacement.

- Category: Core
- Version: 3.2.31
- Access: Free
- Docs: https://functionstore.tools/docs/fns-updater/

## What it does

- **Check for updates**: Compares every installed package with the published release, from the Updates tab or quick-launch, downloading only a small manifest.
- **Update only changed packages**: Fetches only the packages that changed from the store, verifies each download's hash and replaces just those, leaving uninstalled packages uninstalled.
- **Settings kept across updates**: Saves every tool's settings before anything is replaced, and each replaced tool comes back with them.
- **Store for offline installs**: Keeps the whole release in this machine's store, so Pick Tools works without an internet connection.
- **Patreon sign-in and licence keys**: Holds this machine's Patreon sign-in and Gumroad licence keys; the token lives in the operating system keystore, never in the project.
- **Release notes after an update**: A pass that updated something prints the release and its notes in the Textport; the Updates tab keeps them, and one switch turns the line off.
- **Install agent skill**: The Install agent skill command copies a reference to every installed package (promoted methods, commands, hotkeys, parameters, the registries) into the project's .claude/skills folder or your user skills folder, so a coding agent such as Claude Code knows the toolkit before it touches the project.

## Reach it

`op.FNS_UPDATER` is its global shortcut: call its promoted methods on that object from anywhere in the project.

## Promoted API

- `Account()`: The stored account record, or None.
- `AgentSkillFolder()`: Where the agent skill lives on this machine: <user palette>/FNSTools/agent-skill, or '' when this install has no user palette folder.
- `AuthStatus()`: A one-line account status for the UI: signed out, or the tier label and the package count.
- `BaseUrl()`: The manifest base this pass should use.
- `BestVariant(name, manifest=None)`: The highest build of `name` this account holds: 'base', or a variant id whose product (FNS_Foo.pro) the account is entitled to, ranked by its tier's place in the ladder.
- `CachedToken()`: A still-valid download token, or ''.
- `CancelPending()`: Stop waiting on a sign-in or a membership check (the picker's Cancel).
- `Check(_=None)`: Pulse handler for the Check parameter: CheckUpdates() while Active.
- `CheckForUpdates()`: Check the store for FunctionStore tool updates.
- `CheckUpdates(target=None)`: Fetch the manifest, then compare.
- `CommunityList()`: The curated list, from its cached copy.
- `Compare(target=None)`: What this project has vs what the store publishes.
- `DiscoveredBase()`: Where discovery says the manifest lives, or '' if it has never successfully been read on this machine.
- `Drain()`: Public entry so a stalled pass can be nudged from the textport.
- `DropCachedToken()`: Forget the cached download token.
- `Entitlements()`: Package names this install may download.
- `FamilyFolder()`: Where the FNS family's operators live: <user palette>/FNSTools/FNS, or '' when this install has no user palette folder.
- `FindStandalone(target=None, _index=None)`: Standalone copies of global tools anywhere in this project.
- `GateUrl()`: The entitlement gate's base URL (the Gateurl parameter, the production gate by default).
- `InstallAgentSkill(where: Literal['project', 'user'] = 'project', agents_md: bool = False)`: Copy the FNSTools agent skill into this project or your user skills folder.
- `InstallCommunityPackage(name, target=None)`: Install a tdp highlight into the project's venv and place its tox in `target`.
- `Installed(target=None)`: package -> {sha256, release, when} as recorded at install time.
- `IsApplying()`: Is a pass replacing packages right now?
- `IsEntitled(package)`: Whether the stored account holds a package.
- `IsSignedIn()`: Whether an account record is stored on this install.
- `IsUpdatable` (attribute)
- `KeepStore()`: Mirror the rest of the release into the store, when Keepstore says so and no job is running: what RefreshStore returns, or why not.
- `MissingFor(package)`: What to TELL someone who cannot have this package -- naming the ROUTES, not just the refusal: the tier it unlocks at (or higher; the ladder grants upward) and, where a Gumroad row exists, the lifetime key.
- `Notices()`: Messages the discovery document wants every install to see.
- `OnAuthCallback(token, cn='', code='')`: The gate redirected back to loopback.
- `OnClaimResponse(statusCode, data)`: Web Client DAT callback for /session/claim.
- `OnDownloadAborted(callbackInfo)`: Downloader callback for a failed fetch: try the next discovery pin, classify a missing signature, or record the artifact failure.
- `OnFileDownloaded(callbackInfo)`: Dispatch by filename -- the downloader is shared, so the arriving file says what it was for.
- `OnRecheckResponse(statusCode, data)`: Web Client DAT callback for /session/recheck.
- `OnRedeemResponse(statusCode, data)`: Web Client DAT callback for the licence redeem request: store the products a key unlocks, or report the refusal.
- `OnRevokeResponse(statusCode, data)`: Web Client DAT callback for /session/revoke.
- `OnTokenResponse(statusCode, data)`: Web Client DAT callback for /token/download.
- `PlaceCommunityTool(name, target=None)`: Download one community tool and place it in the project.
- `Plusactive` (property): True when this install holds at least one entitled package.
- `PythonEnvStatus()`: Whether the project can take a tdp install: `ready` with the env, or where TD's environment manager stands (`none`, `creating`, `error`).
- `RebuildPaletteIndex()`: Regenerate <userPalette>/paletteData.json from a directory walk and ask TD to re-read it.
- `Recheck(callback=None)`: Ask the gate to re-read entitlement from Patreon RIGHT NOW.
- `RecordInstalled(name, sha256, release='', target=None)`: Upsert one package's install-time hash.
- `RedeemKey(key=None, product=None, package=None)`: Redeem one Gumroad licence key.
- `Redeemlicense(par)`: Pulse handler for the Redeemlicense parameter: RedeemKey().
- `RefreshCommunity()`: Fetch the curated list.
- `RefreshStore(names=None)`: Fetch the manifest, then artifacts whose bytes differ.
- `Refreshstore(_=None)`: Pulse handler for the Refreshstore parameter: RefreshStore().
- `RequestToken(callback=None)`: Ask the gate for a download token.
- `SetUpPythonEnv()`: Give the project a Python environment with TouchDesigner's own TDPyEnvManager: drop it at `/` and switch it Active, which shows Derivative's disclaimer (their consent step, never bypassed), then press its Create vEnv.
- `SignIn()`: Open the browser and listen on loopback for the gate to hand back a device token.
- `SignOut()`: Revoke the device session at the gate, best effort, and forget the account locally.
- `Signin(par)`: Pulse handler for the Signin parameter: SignIn().
- `Signout(par)`: Pulse handler for the Signout parameter: SignOut().
- `StoreFolder()`: Machine-wide package store.
- `StoreManifest()`: What the store holds, as of its last refresh.
- `StoreStatus()`: What the store actually holds, verified against its manifest.
- `SyncAgentSkillFolder()`: Lay the agent skill bundle out in the agent skill folder from the transport document (the store's copy, or this source checkout's own build): every file written where its text differs, anything else under the bundle folder removed.
- `SyncFamilyFolder()`: Mirror every family member the store holds into the family folder (tox plus sidecar, public names), drop what no longer belongs, let TDFam re-read the folder and TD's Palette re-read its index.
- `TakeOver(path, confirm=False, target=None)`: Bring one standalone copy of a global tool under the toolkit.
- `Update(_=None)`: Pulse handler for the Update parameter: UpdateProject() while Active.
- `UpdateProject(names=None, target=None)`: Fetch the manifest, pull only the artifacts THIS project needs, then replace those packages.
- `UpdateTools()`: Download and install available tool updates.

## Commands

- **Check for updates** (id `checkforupdates`): Check the store for FunctionStore tool updates. Method `CheckForUpdates`.
- **Install agent skill** (id `installagentskill`): Copy the FNSTools agent skill into this project or your user skills folder Method `InstallAgentSkill`. Params: `where: menu = 'project'`, `agents_md: toggle = False`.
- **Update tools** (id `updatetools`): Download and install available tool updates. Method `UpdateTools`.

## Hotkeys

None.

## Alternative for

None.

## Requires

Nothing.

## Parameters

### Custom

- **Base URL** (`par.Baseurl`, Str): Where the published manifest lives. Fetches <Base URL>/manifest.json; artifact URLs come from that manifest, pinned to their release. A local folder or file:// path works too, which is how the flow is exercised without a bucket.
- **Enabled** (`par.Active`, Toggle), default `off`: Master switch for the Check and Update pulses.
- **Use Discovery** (`par.Usediscovery`, Toggle), default `on`: Resolve the manifest location from the pinned discovery document instead of trusting Base URL. Leave on: it is what lets the bucket move without a component update, and it carries the minimum-version and notice channel. Turning it off pins this install to Base URL forever. A local or file:// Base URL always wins regardless.
- **Store Folder** (`par.Storefolder`, Folder): Machine-wide package store the manifest and artifacts are fetched into. Blank means <user palette>/FNSTools/store.
- **Target** (`par.Target`, COMP), default `parent()`: The toolkit container whose packages are compared and updated.
- **Show Download Progress** (`par.Showprogress`, Toggle), default `off`: Open the downloader's progress window while files are fetched.
- **Show Notes After Update** (`par.Shownotes`, Toggle), default `on`: After an update pass finishes, the Textport gets one line naming the release and its notes. Turn this off to skip it; the notes stay readable on the Hub's Updates tab either way. This is never a popup and never fires on project start. Roams with your settings.
- **Keep the Whole Release in the Store** (`par.Keepstore`, Toggle), default `on`: After an install or an update pass, also download the rest of the release into this machine's store (about 12 MB), so Pick Tools works offline and everything the store can offer is already here. Off: only what you install is fetched.
- **Refresh Store** (`par.Refreshstore`, Pulse): Fetch the manifest and every artifact whose bytes differ into the store. Machine-wide: no project is touched.
- **Check for Updates** (`par.Check`, Pulse): Fetch the manifest and compare it against this project's install record. Cheap: no artifacts are downloaded.
- **Status** (`par.Status`, Str): Result of the last check, refresh or update pass.
- **Update This Project** (`par.Update`, Pulse): Fetch the artifacts this project needs and replace only the packages whose bytes differ. Never installs a package you did not choose.
- **Gate URL** (`par.Gateurl`, Str): Where entitlement is checked and gated packages are fetched from. Placeholder until the gate is deployed; it is the only address this component knows for paid downloads.
- **Sign In** (`par.Signin`, Pulse): Open your browser to sign in with Patreon. Nothing secret is stored in this project: the token lives in the operating system keystore, locked to this machine and this user.
- **Sign Out** (`par.Signout`, Pulse): Forget this machine's entitlement. Packages you already installed are untouched, and only future paid downloads stop.
- **Account** (`par.Authstatus`, Str), default `signed out`: Who this install is signed in as and how many paid packages the account covers. Read-only.
- **Licence Key** (`par.Licensekey`, Str): A Gumroad licence key. Keys are per tool, so redeeming another one ADDS to this account rather than replacing it.
- **Licence Product** (`par.Licenseproduct`, Str): The Gumroad product id the key above belongs to. Shown on the product page you bought it from.
- **Redeem Licence** (`par.Redeemlicense`, Pulse): Check the licence key with the gate and add what it unlocks to this account.
