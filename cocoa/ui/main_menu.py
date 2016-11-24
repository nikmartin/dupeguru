ownerclass = 'AppDelegate'
ownerimport = 'AppDelegate.h'

result = Menu("")
appMenu = result.addMenu("dupeGuru")
fileMenu = result.addMenu("File")
editMenu = result.addMenu("Edit")
actionMenu = result.addMenu("Actions")
owner.columnsMenu = result.addMenu("Columns")
modeMenu = result.addMenu("Mode")
windowMenu = result.addMenu("Window")
helpMenu = result.addMenu("Help")

appMenu.addItem("About dupeGuru", Action(owner, 'showAboutBox'))
appMenu.addSeparator()
appMenu.addItem("Preferences...", Action(owner, 'showPreferencesPanel'), 'cmd+,')
appMenu.addSeparator()
NSApp.servicesMenu = appMenu.addMenu("Services")
appMenu.addSeparator()
appMenu.addItem("Hide dupeGuru", Action(NSApp, 'hide:'), 'cmd+h')
appMenu.addItem("Hide Others", Action(NSApp, 'hideOtherApplications:'), 'cmd+alt+h')
appMenu.addItem("Show All", Action(NSApp, 'unhideAllApplications:'))
appMenu.addSeparator()
appMenu.addItem("Quit dupeGuru", Action(NSApp, 'terminate:'), 'cmd+q')

fileMenu.addItem("Load Results...", Action(None, 'loadResults'), 'cmd+o')
owner.recentResultsMenu = fileMenu.addMenu("Load Recent Results")
fileMenu.addItem("Save Results...", Action(None, 'saveResults'), 'cmd+s')
fileMenu.addItem("Export Results to XHTML", Action(owner.model, 'exportToXHTML'), 'cmd+shift+e')
fileMenu.addItem("Export Results to CSV", Action(owner.model, 'exportToCSV'))
fileMenu.addItem("Clear Picture Cache", Action(owner, 'clearPictureCache'), 'cmd+shift+p')

editMenu.addItem("Mark All", Action(None, 'markAll'), 'cmd+a')
editMenu.addItem("Mark None", Action(None, 'markNone'), 'cmd+shift+a')
editMenu.addItem("Invert Marking", Action(None, 'markInvert'), 'cmd+alt+a')
editMenu.addItem("Mark Selected", Action(None, 'markSelected'), 'ctrl+cmd+a')
editMenu.addSeparator()
editMenu.addItem("Cut", Action(None, 'cut:'), 'cmd+x')
editMenu.addItem("Copy", Action(None, 'copy:'), 'cmd+c')
editMenu.addItem("Paste", Action(None, 'paste:'), 'cmd+v')
editMenu.addSeparator()
editMenu.addItem("Filter Results...", Action(None, 'focusOnFilterField'), 'cmd+alt+f')

actionMenu.addItem("Start Duplicate Scan", Action(owner, 'startScanning'), 'cmd+d')
actionMenu.addSeparator()
actionMenu.addItem("Send Marked to Trash...", Action(None, 'trashMarked'), 'cmd+t')
actionMenu.addItem("Move Marked to...", Action(None, 'moveMarked'), 'cmd+m')
actionMenu.addItem("Copy Marked to...", Action(None, 'copyMarked'), 'cmd+alt+m')
actionMenu.addItem("Remove Marked from Results", Action(None, 'removeMarked'), 'cmd+r')
actionMenu.addItem("Re-Prioritize Results...", Action(None, 'reprioritizeResults'))
actionMenu.addSeparator()
actionMenu.addItem("Remove Selected from Results", Action(None, 'removeSelected'), 'cmd+backspace')
actionMenu.addItem("Add Selected to Ignore List", Action(None, 'ignoreSelected'), 'cmd+g')
actionMenu.addItem("Make Selected into Reference", Action(None, 'switchSelected'), 'cmd+arrowup')
actionMenu.addSeparator()
actionMenu.addItem("Open Selected with Default Application", Action(None, 'openSelected'), 'cmd+return')
actionMenu.addItem("Reveal Selected in Finder", Action(None, 'revealSelected'), 'cmd+alt+return')
actionMenu.addItem("Invoke Custom Command", Action(None, 'invokeCustomCommand'), 'cmd+shift+c')
actionMenu.addItem("Rename Selected", Action(None, 'renameSelected'), 'enter')

modeMenu.addItem("Show Dupes Only", Action(None, 'togglePowerMarker'), 'cmd+1')
modeMenu.addItem("Show Delta Values", Action(None, 'toggleDelta'), 'cmd+2')

windowMenu.addItem("Results Window", Action(owner, 'showResultWindow'))
windowMenu.addItem("Folder Selection Window", Action(owner, 'showDirectoryWindow'))
windowMenu.addItem("Ignore List", Action(owner, 'showIgnoreList'))
windowMenu.addItem("Details Panel", Action(None, 'toggleDetailsPanel'), 'cmd+i')
windowMenu.addItem("Quick Look", Action(None, 'toggleQuicklookPanel'), 'cmd+l')
windowMenu.addSeparator()
windowMenu.addItem("Minimize", Action(None, 'performMinimize:'))
windowMenu.addItem("Zoom", Action(None, 'performZoom:'))
windowMenu.addItem("Close Window", Action(None, 'performClose:'), 'cmd+w')
windowMenu.addSeparator()
windowMenu.addItem("Bring All to Front", Action(None, 'arrangeInFront:'))

helpMenu.addItem("dupeGuru Help", Action(owner, 'openHelp'), 'cmd+?')
helpMenu.addItem("dupeGuru Website", Action(owner, 'openWebsite'))
