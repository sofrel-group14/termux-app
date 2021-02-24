# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: Termux app

URL: https://github.com/termux/termux-app (original repo)

Termux is an Android application that emulates a Linux terminal. There are
several Linux packages that you can additionally install for more functionality.
Among other things you can use Python and ssh.

NCLOC (by lizard): 10646 (10475 if considering only Java)

## Onboarding experience

Did it build and run as documented?
    
See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.


## Complexity

1. What are your results for ten complex functions?
   * Did all methods (tools vs. manual count) get the same result?
   * Are the results clear?
2. Are the functions just complex, or also long?
3. What is the purpose of the functions?
4. Are exceptions taken into account in the given measurements?
5. Is the documentation clear w.r.t. all the possible outcomes?

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
| TerminalEmulator.java:processByte   		 	| [9](processBytes.jpg) | [21](processBytes2.jpg) | 21     |
| TerminalEmulator.java:selectGraphicRendition  | ??           | ??           | 51   |
| TermuxActivity.java:onContextItemSelected  	| [9](onContextItemSelected.png)  | ??           |  20  |
| TermuxViewClient.java:onKeyDown   			| ??           | ??           |  24   |

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?
