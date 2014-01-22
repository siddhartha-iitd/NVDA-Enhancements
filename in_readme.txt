This release of nvda is published by saksham and is signed by a certificate issued by saksham. To be able to run this release of NVDA, you must install the saksham public key using the install-cert.bat file supplied here. This can only be run as an administrator on a machine.
To run as admin, right click on the install-cert.bat file or in windows explorer, press the application key when install-cert.bat is selected and select run as administrator.
Alternatively, open a command prompt as an administrator. cd to the folder containing this file and run install-cert.bat. Doing this will help you see any errors generated while running the bat file.

This document will contain a running list of the fixes included in the cumulative build. the cumulative build is based on the "next" nvda branch with all the bug fixes done by the India team so far even if they haven't yet been accepted by the NVDA developers.

Jan 21, 2013
- 3680 : read all formula in excel sheet (nvda+f7)
- 3681 : read all comments in excel sheet (nvda+f7)
  -- Finished implementation. Lot of 'viewing modes' supported, 
     like Cells-Flat, Row-Cells, Column-Cells etc.
    

Jan 07, 2013
- 3231 :  nvda incorrectly speaks previously entered but later deleted characters when the space bar is pressed.

- Issue: Beeps in snapshot build
  Solution: Version number has to start with numeral, to disable the testmode.
            Version format changed to yyyymmmdd_in_next


Dec 03, 2013
- 3680 : read all formula in excel sheet
- 3681 : read all comments in excel sheet
  -> Pressing NVDA+f7 will print a dialog box. This has a choice to show cells with comment or formula
     Pressing 'Enter' at any selection in the tree will close dialog and select cell or area

Nov 19, 2013 
- REPATCH: #2920 : Excel: Reading and editing of comments currently not possible


Oct 2013
  Redoing to base all the feature branches and in_next branch on master.
  All features will have to repatched now

sep 21, 2013
- #3538: Office 2010, NVDA now reads the selected symbols in the insert|symbols dialog box in word and excel 2010
- #2921: Excel , NVDA will say 'has comment' if cell has comment on it

Sep 18, 2013
- #2920 : Excel: Reading and editing of comments currently not possible
- #3043 : in Excel, Contrl-A doesn't notify the change in selection
Aug 30, 2013
- #1938 : In word 2007 and 2010, NVDA does not automatically speak the error text in the spell checker dialog after the first time the dialog is launched if the focus is already in the error text field.

Aug 23, 2013
- #2446: partially fixed to read the bullet types. List levels not currently added.
- Ctrl + up and down arrows in word now skip blank paragraphs.
- #3431: Spell check in word 2010 now reads the correct context error text instead of reading all bolded text in the context.
- #3290: Bulleted text is now correctly read with ctrl+up and down arrows
- #3288: sentence reading in word
- #1686: protected documents in word 2010
- #649: status bar in word office 2010
- #2816: auto complete suggested contacts in outlook 2010
- 2047: language detection in word.

