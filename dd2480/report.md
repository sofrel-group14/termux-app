# Report for assignment 3

## Project

Name: Termux app

URL: https://github.com/termux/termux-app (original repo)

Termux is an Android application that emulates a Linux terminal. There are
several Linux packages that you can additionally install for more functionality.
Among other things you can use Python and ssh.

NCLOC (by lizard): 10646 (10475 if considering only Java)

## Onboarding experience

There was pretty much no documentation available at all, so we had to figure it out ourselves. These are the steps required to get it to run.

1. Install and set up the correct SDK and NDK in IntelliJ (note: SDK version 28, and NDK version 21.1.6352462).
    - The SDK version was not documented, we had to find the `targetSdkVersion` in `gradle.properties`.
2. Create a `local.properties`-file with SDK location (ex: `sdk.dir=/Users/name/Library/Android/sdk`). This was automatically generated the first time (when cloning the original repo), but had to be done manually when cloning the forked repo.
3. Change Gradle version from `4.1.1` to `4.0.2`. in `build.gradle` (`classpath 'com.android.tools.build:gradle:4.0.2'`)
4. Change Robolectric version from `4.4` to `4.5` in `build.gradle (:app)` (`testImplementation 'org.robolectric:robolectric:4.5'`)
5. Set up the phone-emulator (by choosing a Device/AVD in IntelliJ).
6. To run the tests, run `./gradlew test` (also not documented; we had to find this in the Github Actions).

**NOTE:** You cannot store NDK-files in paths containing spaces or parentheses.</br>
**NOTE:** You cannot store the project in paths containing spaces.

## Complexity

>> 1. What are your results for ten complex functions?
>>    * Did all methods (tools vs. manual count) get the same result?
>>    * Are the results clear?
>> 2. Are the functions just complex, or also long?
>> 3. What is the purpose of the functions?
>> 4. Are exceptions taken into account in the given measurements?
>> 5. Is the documentation clear w.r.t. all the possible outcomes?

These were the functions that generated warnings in lizard, they all have CCN > 15:
```
================================================
  NLOC    CCN   token  PARAM  length  location  
------------------------------------------------
     151    112   1112      4     187 KeyHandler::getCode@156-342@./terminal-emulator/src/main/java/com/termux/terminal/KeyHandler.java
     291    105   1764      1     334 TerminalEmulator::processCodePoint@474-807@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     278     76   1634      1     319 TerminalEmulator::doCsi@1352-1670@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     132     52    538      1     142 TerminalEmulator::emitCodePoint@2117-2258@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     100     51    751      0     105 TerminalEmulator::selectGraphicRendition@1673-1777@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     121     49    921      6     152 TerminalBuffer::resize@161-312@./terminal-emulator/src/main/java/com/termux/terminal/TerminalBuffer.java
     126     46    859      1     143 TerminalEmulator::doOscSetTextParameters@1809-1951@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     114     43    567      3     133 TermuxViewClient::onCodePoint@125-257@./app/src/main/java/com/termux/app/TermuxViewClient.java
      84     41    354      2      96 TerminalEmulator::doDecSetOrReset@1016-1111@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
     142     35   1077      2     175 TermuxActivity::onServiceConnected@391-565@./app/src/main/java/com/termux/app/TermuxActivity.java
      77     29    711      7      93 TerminalRenderer::render@57-149@./terminal-view/src/main/java/com/termux/view/TerminalRenderer.java
      45     29    306      3      57 TerminalView::inputCodePoint@637-693@./terminal-view/src/main/java/com/termux/view/TerminalView.java
     118     28    854      1     136 ExtraKeysView::reload@238-373@./app/src/main/java/com/termux/app/ExtraKeysView.java
      55     27    482      2      67 TerminalView::onKeyDown@569-635@./terminal-view/src/main/java/com/termux/view/TerminalView.java
      82     26    476      1      83 TerminalEmulator::doCsiQuestionMark@932-1014@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
      87     25    442      1      89 TerminalEmulator::doEsc@1233-1321@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
      42     24    391      3      49 TermuxViewClient::onKeyDown@59-107@./app/src/main/java/com/termux/app/TermuxViewClient.java
      75     24    617      3     110 TerminalRow::setChar@126-235@./terminal-emulator/src/main/java/com/termux/terminal/TerminalRow.java
     104     24    694      2     125 TerminalView::TerminalView@101-225@./terminal-view/src/main/java/com/termux/view/TerminalView.java
      68     24    379      3      84 TerminalView::SelectionModifierCursorController::updatePosition@1298-1381@./terminal-view/src/main/java/com/termux/view/TerminalView.java
      46     21    315      1      64 TerminalEmulator::processByte@409-472@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
      82     20    608      1      86 TermuxActivity::onContextItemSelected@860-945@./app/src/main/java/com/termux/app/TermuxActivity.java
      94     20    796      2     110 TermuxInstaller::setupIfNeeded@50-159@./app/src/main/java/com/termux/app/TermuxInstaller.java
      40     20    341      6      44 TerminalBuffer::getSelectedText@60-103@./terminal-emulator/src/main/java/com/termux/terminal/TerminalBuffer.java
      68     19    490      8      89 create_subprocess@25-113@./terminal-emulator/src/main/jni/termux.c
      73     18    461      1     114 TerminalEmulator::doDeviceControl@810-923@./terminal-emulator/src/main/java/com/termux/terminal/TerminalEmulator.java
      41     17    335      2      53 BackgroundJob::setupProcessArgs@189-241@./app/src/main/java/com/termux/app/BackgroundJob.java
      70     17    541      2      81 TermuxOpenReceiver::onReceive@28-108@./app/src/main/java/com/termux/app/TermuxOpenReceiver.java
      82     17    478      1     115 TerminalView::onCreateInputConnection@257-371@./terminal-view/src/main/java/com/termux/view/TerminalView.java
      64     16    567      3      82 TermuxService::onStartCommand@99-180@./app/src/main/java/com/termux/app/TermuxService.java
      14     16    103      1      20 WcWidth::width@488-507@./terminal-emulator/src/main/java/com/termux/terminal/WcWidth.java
      59     16    581      9      65 Java_com_termux_terminal_JNI_createSubprocess@115-179@./terminal-emulator/src/main/jni/termux.c
      65     16    616     13      82 TerminalRenderer::drawTextRun@151-232@./terminal-view/src/main/java/com/termux/view/TerminalRenderer.java
```

We chose 5 of those to manually calculate CCN, with the following results (with exceptions):

| Function           				  			| First calc   | Second calc  | lizard |
| --------------------------------------------- |:------------:| ------------:| ------:|
| TermuxOpenReceiver.java:onReceive  		 	| [13](onReceive_calc1.png) | ??           | 17  |
| TerminalEmulator.java:processByte   		 	| [10](processBytes.jpg) | [21](processBytes2.jpg) | 21     |
| TerminalEmulator.java:selectGraphicRendition  | 40  | ??           | 51   |
| TermuxActivity.java:onContextItemSelected  	| [9](onContextItemSelected.png)  | ??           |  20  |
| TermuxViewClient.java:onKeyDown   			| [24](onKeyDown.png)   | ??           |  24   |

### After Cyrille's input
| Function           				  			| First calc   | Second calc  | lizard |
| --------------------------------------------- |:------------:| ------------:| ------:|
| TermuxOpenReceiver.java:onReceive  		 	| 17           | 17           | 17     |
| TerminalEmulator.java:processByte   		 	| 20           | 20           | 21     |
| TerminalEmulator.java:selectGraphicRendition  | 50           | 50           | 51     |
| TermuxActivity.java:onContextItemSelected  	| 19           | 19          | 20     |
| TermuxViewClient.java:onKeyDown   			| 23           | 23           | 24     |

## Refactoring

Detailed below are plans for refactoring five different complex functions.

#### 1. Refactoring TermuxOpenReceiver.java:onReceive

```java
//...
final String intentAction = intent.getAction() == null ? Intent.ACTION_VIEW : intent.getAction();
switch (intentAction) {
    case Intent.ACTION_SEND:
    case Intent.ACTION_VIEW:
        // Ok.
        break;
    default:
        Log.e(EmulatorDebug.LOG_TAG, "Invalid action '" + intentAction + "', using 'view'");
        break;
}
// ...
```

Breaking out this switch-statement to a new function, say `verifyIntentAction`, would reduce the CC by 3.

```java
public void verifyIntentAction(int intentAction) {
    switch (intentAction) {
        case Intent.ACTION_SEND:
        case Intent.ACTION_VIEW:
            // Ok.
            break;
    default:
        Log.e(EmulatorDebug.LOG_TAG, "Invalid action '" + intentAction + "', using 'view'");
        break;
}
```

Further, we have the following block of code:

```java
final File fileToShare = new File(filePath);
//...
String contentTypeToUse;
if (contentTypeExtra == null) {
    String fileName = fileToShare.getName();
    int lastDotIndex = fileName.lastIndexOf('.');
    String fileExtension = fileName.substring(lastDotIndex + 1);
    MimeTypeMap mimeTypes = MimeTypeMap.getSingleton();
    // Lower casing makes it work with e.g. "JPG":
    contentTypeToUse = mimeTypes.getMimeTypeFromExtension(fileExtension.toLowerCase());
    if (contentTypeToUse == null) contentTypeToUse = "application/octet-stream";
} else {
    contentTypeToUse = contentTypeExtra;
}
```
which seems to extract the MIME-type to use based on the file path.
This could also be broken out to a different function, say `getMimeTypeFromFile`.
This would reduce the CC by 3, and also the LOC quite a bit (another way to measure complexity).

#### 2. Refactoring TermuxActivity.java:onContextItemSelected

When looking at onContextItemSelected the first aspect I would refactor this case statement:

```java
case CONTEXTMENU_SHARE_TRANSCRIPT_ID:
    if (session != null) {
        Intent intent = new Intent(Intent.ACTION_SEND);
        intent.setType("text/plain");
        String transcriptText = session.getEmulator().getScreen().getTranscriptTextWithoutJoinedLines().trim();
        // See https://github.com/termux/termux-app/issues/1166.
        final int MAX_LENGTH = 100_000;
        if (transcriptText.length() > MAX_LENGTH) {
            int cutOffIndex = transcriptText.length() - MAX_LENGTH;
            int nextNewlineIndex = transcriptText.indexOf('\n', cutOffIndex);
            if (nextNewlineIndex != -1 && nextNewlineIndex != transcriptText.length() - 1) {
                cutOffIndex = nextNewlineIndex + 1;
            }
            transcriptText = transcriptText.substring(cutOffIndex).trim();
        }
        intent.putExtra(Intent.EXTRA_TEXT, transcriptText);
        intent.putExtra(Intent.EXTRA_SUBJECT, getString(R.string.share_transcript_title));
        startActivity(Intent.createChooser(intent, getString(R.string.share_transcript_chooser_title)));
    }
```
The point of this case statement is to start a new Activity which we can see on line 884. The first thing I would change is putting the entire `if(session != null)` in a new function since the entire point of it is to start a new Activity, which is not directly related to the function at hand and this would also reduce the CCN quite a bit. I would also probably change line 873-881 in a new function since the entire point of that block is to set the `transcriptText` and I think that having a method for calculating the `transcriptText` and returning it would look better. This would reduce the the CCN by 4.



```java
case CONTEXTMENU_TOGGLE_KEEP_SCREEN_ON: {
    if(mTerminalView.getKeepScreenOn()) {
        mTerminalView.setKeepScreenOn(false);
        mSettings.setScreenAlwaysOn(this, false);
    } else {
        mTerminalView.setKeepScreenOn(true);
        mSettings.setScreenAlwaysOn(this, true);
    }
    return true;
}
case CONTEXTMENU_AUTOFILL_ID: {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        AutofillManager autofillManager = getSystemService(AutofillManager.class);
        if (autofillManager != null && autofillManager.isEnabled()) {
            autofillManager.requestAutofill(mTerminalView);
        }
    }
}
```

I would also refactor these two switch statements by breaking them into new methods. For example in 924-933: this can be a method of its own since it only deals with toggling if the screen is always on or not.This would reduce the CCN by 1. The second switch statement I would break out since it deals with some autofill manager which can easily be put in a new function since the functionality is so specific This would reduce the CCN by 3. 

#### 3. Refactoring TerminalEmulator::selectGraphicRendition

This function consisted of a long if-else chain. Parts of this chain could be extracted into a hashmap and indexed for the appropriate condition. This reduced the CCN from 51 to 36.

[Refactoring here.](https://github.com/sofrel-group14/termux-app/commit/ba0d9a1d8848e57437e21f66b0da405162de95de#diff-d7feb4ab2a600dd7816f1744e01a8a82926522818b465a7e3a3216b62f01d5ceR1673-R1694)

#### 4. Refactoring TerminalEmulator::processCodePoint

`processCodePoint` is one of the functions with the highest CCN, as can be seen in [Complexity](#complexity). If we take a look at this function, we can see that it contains one huge switch statement, with several switch statements nested in its cases (up to 4 levels of nesting). In its current state it is hard to get a good overview and understand the function, especially when there are several nested switches. Firstly, I think the whole function could be moved to its own class. The `TerminalEmulator` class is already 2000 lines long, and by separating `processCodePoint` into smaller parts in another class would reduce this by 330 lines.

For example, by moving the switch statement in the default case at line 539 into a separate function you would decrease the CCN by around 65 or so, which would half the CCN. This function could be broken up further to decrease its complexity in turn.

#### 5. Refactoring TerminalEmulator::emitCodePoint
`emitCodePoint` is one of the functions with the highest CCN, as can be seen in [Complexity](#complexity). There are a myriad of different methods you can utilize to reduce the CCN. In this case, a simple but effective one will look at the switch statement. This switch statement has 33 cases. By moving the switch statement into a separate function, would around halve the CCN. Furthermore, this specific statement lends itself to extraction to a hashmap structure quite well. This would further decrease the complexity of the code.

[Refactoring here.](https://github.com/sofrel-group14/termux-app/pull/15/commits/a744eabc0534d943bed340af3230197681d3c8b7)


## Coverage

The manual coverage was generated by instrumenting the code (adding print statements with unique IDs for each identified branch).
Then, a [Python script](https://github.com/sofrel-group14/termux-app/blob/andreas-branch-coverage/cov.py) was used to generate
a summary of taken branches (see below for example input to (and example output from) the script).
For an example of the instrumented code, see getSelectedText on line 60 [here](https://github.com/sofrel-group14/termux-app/blob/da6e1428d5327d62f1bb3c26bc45448ae51e9605/terminal-emulator/src/main/java/com/termux/terminal/TerminalBuffer.java).

```python
"""
USAGE:
1) Add ID to each branch in the function, and execute:
	System.err.println("TEST_COVERAGE_getCodeFromTermcap:1");
   for each branch (ID = 1 in example above).

2) Run tests with -i flag to get error printouts, save output to file.
   $ ./gradlew test -i &> testlog.txt

3) Grep the file to get relevant lines about test coverage, and save them to file.
   $ cat testlog.txt | grep -e "TEST_COVERAGE_getCodeFromTermcap" > coverage.txt

4) Run this file to get coverage printouts.
   $ python3 cov.py
"""
```

#### Example input (abbreviated) to Python script:
```
coverage.txt

...
TEST_COVERAGE_getSelectedText:41
TEST_COVERAGE_getSelectedText:42
TEST_COVERAGE_getSelectedText:43
TEST_COVERAGE_getSelectedText:6
TEST_COVERAGE_getSelectedText:8
TEST_COVERAGE_getSelectedText:12
...
```

#### Example output from Python script:
```
Andreass-MBP:termux-app andreaskarrby$ python3 cov.py 
Branch counts:
1: 56
2: 0
3: 56
4: 36
5: 20
6: 136
7: 56
8: 80
9: 56
10: 36
11: 20
12: 80
13: 16
14: 120
15: 0
16: 22
17: 18
18: 4
19: 8
20: 8
21: 0
22: 114
23: 426
24: 144
25: 282
26: 98
27: 38
28: 0
29: 0
30: 0
31: 0
32: 0
33: 0
34: 0
35: 0
36: 0
37: 0
38: 0
39: 0
40: 114
41: 106
42: 60
43: 60
44: 0
45: 46
46: 2
47: 2
48: 2
49: 0
50: 0
51: 6
52: 22
Manually instrumented function: getSelectedText
Branches not taken (IDs): 2, 15, 21, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 44, 49, 50, 
 
Out of 52 branches, 34 were taken (~65%)
```

### Tools

>> Document your experience in using a "new"/different coverage tool.
>>
>> How well was the tool documented? Was it possible/easy/difficult to integrate it with your build environment?
>>
>> What kinds of constructs does your tool support, and how accurate is its output?

### Evaluation

>> 1. How detailed is your coverage measurement?

It does not consider ternary operators, and compound if-statements (with &&s and ||s)

>> 2. What are the limitations of your own tool?

Since it's based on manual instrumentation, it's limited in the sense that when code is changed, we would have to manually change the instrumentation code.

>> 3. Are the results of your tool consistent with existing coverage tools?

No since we don't consider ternary operators

## Coverage improvement

>> Show the comments that describe the requirements for the coverage.

Report of old coverage:
```
Manually instrumented function: GETCODE
Branches not taken (IDs): 2, 21, 22, 23, 24, 25, 29, 30, 31, 35, 36, 37, 38, 42, 43, 63, 64, 

Out of 64 branches, 47 were taken (~73%)
```

# Report of new coverage:

```
Manually instrumented function: GETCODE
Branches not taken (IDs): 24, 31, 64,

Out of 64 branches, 61 were taken (~95%)
```

### Test cases added
- Taqui added: https://github.com/sofrel-group14/termux-app/commit/74e3782bc8a06c7efb2824f7f18c4f404336ef37
- Axel added: https://github.com/sofrel-group14/termux-app/commit/ed2142ddaff719dde418aed2e0f674ab38462046 (see the file KeyHandlerTest.java at the bottom)
- Andreas added: https://github.com/sofrel-group14/termux-app/commit/032e4c1aa3655c1270544d143a317b09da4e7bf4
- Yannis added: https://github.com/sofrel-group14/termux-app/commit/4448012dbf04a7dc2e3afa433f9bd04a78c20373
- Telo added: https://github.com/sofrel-group14/termux-app/pull/8/commits/8cbd5cdc28f0c707280e19ec1d176a3babe5ec68

## Self-assessment: Way of working

The self assessment was unanimous.

See [this](https://docs.google.com/document/d/1hg5l8HvAqXFEaWk-7z9bNG7bG17T9uXoqnSrAjUhwm0/edit?usp=sharing) document.

## Overall experience

- Documentation of code is underrated
- Communication matters - communicate more
- Android Studio brings us sadness

## Statement of contributions

Telo added four tests, did some manual CCN calculations, did one of two refactorings, added instrumentation to one function, and added one refactoring plan. He is aiming for P+.

Taqui added 2 tests, did manaual CCN calculations, added instrumentation to one function, and added one refactoring plan. He is aiming for P.
