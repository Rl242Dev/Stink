#MaxHotkeysPerInterval 100
#SingleInstance Force

~RButton & LButton:: ;This is just a note
While GetKeyState("RButton", "P") AND GetKeyState("LButton", "P")
{ 
DllCall("mouse_event", uint, 3, int, 0, int, 3, uint, 0, int, 0)
 
DllCall("mouse_event", uint, 3, int, 0, int, 3, uint, 0, int, 0)
Sleep, 2
}
End::ExitApp
Home::suspend