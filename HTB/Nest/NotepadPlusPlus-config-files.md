# NotepadPlusPlus config files

This is in **Data/IT/Configs/NotepadPlusPlus/config.xml**
```xml
<?xml version="1.0" encoding="Windows-1252" ?>
<NotepadPlus>
    <GUIConfigs>
        <!-- 3 status : "large", "small" or "hide"-->
        <GUIConfig name="ToolBar" visible="yes">standard</GUIConfig>
        <!-- 2 status : "show" or "hide"-->
        <GUIConfig name="StatusBar">show</GUIConfig>
        <!-- For all attributs, 2 status : "yes" or "no"-->
        <GUIConfig name="TabBar" dragAndDrop="yes" drawTopBar="yes" drawInactiveTab="yes" reduce="yes" closeButton="no" doubleClick2Close="no" vertical="no" multiLine="no" hide="no" />
        <!-- 2 positions : "horizontal" or "vertical"-->
        <GUIConfig name="ScintillaViewsSplitter">vertical</GUIConfig>
        <!-- For the attribut of position, 2 status : docked or undocked ; 2 status : "show" or "hide" -->
        <GUIConfig name="UserDefineDlg" position="undocked">hide</GUIConfig>
        <GUIConfig name="TabSetting" size="4" replaceBySpace="no" />
        <!--App position-->
        <GUIConfig name="AppPosition" x="662" y="95" width="955" height="659" isMaximized="yes" />
        <!-- For the primary scintilla view,
             2 status for Attribut lineNumberMargin, bookMarkMargin, indentGuideLine and currentLineHilitingShow: "show" or "hide"
             4 status for Attribut folderMarkStyle : "simple", "arrow", "circle" and "box"  -->
        <GUIConfig name="ScintillaPrimaryView" lineNumberMargin="show" bookMarkMargin="show" folderMarkStyle="box" indentGuideLine="show" currentLineHilitingShow="show" Wrap="yes" edge="no" edgeNbColumn="100" wrapSymbolShow="hide" zoom="0" whiteSpaceShow="hide" eolShow="hide" lineWrapMethod="aligned" zoom2="0" />
        <!-- For the secodary scintilla view,
             2 status for Attribut lineNumberMargin, bookMarkMargin, indentGuideLine and currentLineHilitingShow: "show" or "hide"
             4 status for Attribut folderMarkStyle : "simple", "arrow", "circle" and "box" -->
        <GUIConfig name="Auto-detection">yes</GUIConfig>
        <GUIConfig name="CheckHistoryFiles">no</GUIConfig>
        <GUIConfig name="TrayIcon">no</GUIConfig>
        <GUIConfig name="RememberLastSession">yes</GUIConfig>
        <!--
			New Document default settings :
				format = 0/1/2 -> win/unix/mac
				encoding = 0/1/2/3/4/5 -> ANSI/UCS2Big/UCS2small/UTF8/UTF8-BOM
				defaultLang = 0/1/2/..

			Note 1 : UTF8-BOM -> UTF8 without BOM
			Note 2 : for defaultLang :
					0 -> L_TXT
					1 -> L_PHP
					... (see source file)
		-->
        <GUIConfig name="NewDocDefaultSettings" format="0" encoding="0" lang="0" codepage="-1" openAnsiAsUTF8="no" />
        <GUIConfig name="langsExcluded" gr0="0" gr1="0" gr2="0" gr3="0" gr4="0" gr5="0" gr6="0" gr7="0" langMenuCompact="yes" />
        <!--
		printOption is print colour setting, the following values are possible :
			0 : WYSIWYG
			1 : Invert colour
			2 : B & W
			3 : WYSIWYG but without background colour
		-->
        <GUIConfig name="Print" lineNumber="no" printOption="0" headerLeft="$(FULL_CURRENT_PATH)" headerMiddle="" headerRight="$(LONG_DATE) $(TIME)" headerFontName="IBMPC" headerFontStyle="1" headerFontSize="8" footerLeft="" footerMiddle="-$(CURRENT_PRINTING_PAGE)-" footerRight="" footerFontName="" footerFontStyle="0" footerFontSize="9" margeLeft="0" margeTop="0" margeRight="0" margeBottom="0" />
        <!--
                            Backup Setting :
                                0 : non backup
                                1 : simple backup
                                2 : verbose backup
                      -->
        <GUIConfig name="Backup" action="0" useCustumDir="no" dir="" />
        <GUIConfig name="TaskList">yes</GUIConfig>
        <GUIConfig name="SaveOpenFileInSameDir">no</GUIConfig>
        <GUIConfig name="noUpdate" intervalDays="15" nextUpdateDate="20080426">no</GUIConfig>
        <GUIConfig name="MaitainIndent">yes</GUIConfig>
        <GUIConfig name="MRU">yes</GUIConfig>
        <GUIConfig name="URL">0</GUIConfig>
        <GUIConfig name="globalOverride" fg="no" bg="no" font="no" fontSize="no" bold="no" italic="no" underline="no" />
        <GUIConfig name="auto-completion" autoCAction="0" triggerFromNbChar="1" funcParams="no" />
        <GUIConfig name="sessionExt"></GUIConfig>
        <GUIConfig name="SmartHighLight">yes</GUIConfig>
        <GUIConfig name="TagsMatchHighLight" TagAttrHighLight="yes" HighLightNonHtmlZone="no">yes</GUIConfig>
        <GUIConfig name="MenuBar">show</GUIConfig>
        <GUIConfig name="Caret" width="1" blinkRate="250" />
        <GUIConfig name="ScintillaGlobalSettings" enableMultiSelection="no" />
        <GUIConfig name="openSaveDir" value="0" defaultDirPath="" />
        <GUIConfig name="titleBar" short="no" />
        <GUIConfig name="DockingManager" leftWidth="200" rightWidth="200" topHeight="200" bottomHeight="266">
            <FloatingWindow cont="4" x="39" y="109" width="531" height="364" />
            <PluginDlg pluginName="dummy" id="0" curr="3" prev="-1" isVisible="yes" />
            <PluginDlg pluginName="NppConverter.dll" id="3" curr="4" prev="0" isVisible="no" />
            <ActiveTabs cont="0" activeTab="-1" />
            <ActiveTabs cont="1" activeTab="-1" />
            <ActiveTabs cont="2" activeTab="-1" />
            <ActiveTabs cont="3" activeTab="-1" />
        </GUIConfig>
    </GUIConfigs>
    <!-- The History of opened files list -->
    <FindHistory nbMaxFindHistoryPath="10" nbMaxFindHistoryFilter="10" nbMaxFindHistoryFind="10" nbMaxFindHistoryReplace="10" matchWord="no" matchCase="no" wrap="yes" directionDown="yes" fifRecuisive="yes" fifInHiddenFolder="no" dlgAlwaysVisible="no" fifFilterFollowsDoc="no" fifFolderFollowsDoc="no" searchMode="0" transparencyMode="0" transparency="150">
        <Find name="text" />
        <Find name="txt" />
        <Find name="itx" />
        <Find name="iTe" />
        <Find name="IEND" />
        <Find name="redeem" />
        <Find name="activa" />
        <Find name="activate" />
        <Find name="redeem on" />
        <Find name="192" />
        <Replace name="C_addEvent" />
    </FindHistory>
    <History nbMaxFile="15" inSubMenu="no" customLength="-1">
        <File filename="C:\windows\System32\drivers\etc\hosts" />
        <File filename="\\HTB-NEST\Secure$\IT\Carl\Temp.txt" />
        <File filename="C:\Users\C.Smith\Desktop\todo.txt" />
    </History>
</NotepadPlus>
```

This is in **Data/IT/Configs/RU Scanner/RU_config.xml**

```xml
<?xml version="1.0"?>
<ConfigFile xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Port>389</Port>
  <Username>c.smith</Username>
  <Password>fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=</Password>
</ConfigFile>
```

