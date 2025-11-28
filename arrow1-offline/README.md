## **Build Command**
```bash
docker build -t arrow1-offline -f Dockerfile .
```

## **Pytest Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" arrow1-offline pytest
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" arrow1-offline pytest
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" arrow1-offline pytest
```

## **Pre Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" arrow1-offline pre
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" arrow1-offline pre
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" arrow1-offline pre
```

## **Post Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" arrow1-offline post
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" arrow1-offline post
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" arrow1-offline post
```
