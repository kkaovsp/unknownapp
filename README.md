# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

```mermaid
flowchart LR
    %% Primary Actors (Left / Initiators)
    Student["👤 Student"]
    Admin["👤 Admin"]

    subgraph Course Enrollment System
        direction TB
        
        %% Use Cases (Verbs)
        Login(["Log in"])
        CreateProfile(["Create Student Profile"])
        ViewCatalog(["View Course Catalog"])
        RegisterCourse(["Register for Course"])
        DropCourse(["Drop Course"])
        ViewSchedule(["View Student Schedule"])
        Billing(["View Billing Summary"])
        
        ManageStudents(["Manage Students"])
        ManageCourses(["Manage Courses"])
        Logout(["Log out"])
        
        EvaluateCon(["Evaluate Conditions"])
        SaveData(["Save Data"])
    end

    %% Secondary Actors (Right / External Services)
    FS["&lt;&lt;service&gt;&gt;<br>Local File System"]

    %% A. Associations (Base access)
    Student --- Login
    Student --- ViewCatalog
    Student --- RegisterCourse
    Student --- DropCourse
    Student --- ViewSchedule
    Student --- Billing
    Student --- Logout

    Admin --- Login
    Admin --- ViewCatalog
    Admin --- ViewSchedule
    Admin --- Billing
    Admin --- ManageStudents
    Admin --- ManageCourses
    Admin --- Logout

    SaveData --- FS
    Login --- FS

    %% B. Include Relationships (Base -> Included : Mandatory)
    RegisterCourse -.->|"&lt;&lt;include&gt;&gt;"| EvaluateCon
    Logout -.->|"&lt;&lt;include&gt;&gt;"| SaveData

    %% C. Extend Relationships (Extending -> Base : Optional condition)
    CreateProfile -.->|"&lt;&lt;extend&gt;&gt;"| Login
```

### Flowchart of the main workflow

```mermaid
flowchart TD
    Start([Start System]) --> Init[Initialize & Load Data]
    Init --> LoginMenu{Main Login Menu}
    
    LoginMenu -->|1. Student Login| SLogin[Enter Student ID]
    LoginMenu -->|2. Admin Login| ALogin[Enter Password]
    LoginMenu -->|3. Exit| SaveExit[Save Data & Exit]
    
    SaveExit --> Stop([End System])
    
    SLogin --> SCheck{Valid ID / New?}
    SCheck -->|New| SCreate[Create Profile] --> SMenu
    SCheck -->|Valid ID| SMenu{Student Menu}
    SCheck -->|Invalid| LoginMenu
    
    SMenu --> |1-6| SAction[Perform Student Action]
    SAction --> SMenu
    SMenu --> |7. Logout| SLogout[Save Data & Logout]
    SLogout --> LoginMenu
    
    ALogin --> ACheck{Correct Password?}
    ACheck -->|Yes| AMenu{Admin Menu}
    ACheck -->|No| LoginMenu
    
    AMenu --> |1-9| AAction[Perform Admin Action]
    AAction --> AMenu
    AMenu --> |10. Logout| ALogout[Save Data & Logout]
    ALogout --> LoginMenu
```

### Prompts

1. "Try to execute it, read the code, and understand what the program does."
2. "Create a use case diagram that shows the program's functionality. Put the use case diagram in the README.md"
3. Based on what you understand about the program Explain the program to me in Thai
4. "- Based on what you understand about the program, select one use case and create an equivalent Python version of the program. Put the Python program in a new folder called “python.” You can use AI to help you on this, but you must put the prompts you used in the README.md under the section “# Prompts.” on file README.md

   - I select the login case.

