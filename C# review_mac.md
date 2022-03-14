## command list
  - create new project: *dotnet new console -o demo*
  - run proj a.cs, in the same folder: *dotnet run*
  - auto format(no need selecting): *option+shift+f*
  - **[Sublime Text 3 configuration C#:](https://stackoverflow.com/questions/58530006/how-to-run-c-sharp-on-sublime-text-3-on-macos)** 
  > {
    "cmd":      [   "mcs '$file' && mono $file_base_name.exe"   ],
    "shell":        true,
    // error regex credits to Simon | github.com/mightbesimon
    "file_regex":   "^(..[^(]*?)\\(([0-9]*),([0-9]*)\\):? (.*)$",
    "selector":     "source.cs"
}


## tips:
- string"",char''
- compiler internally performs type conversion. e.g.10+"abc"//"10abc"
- 
