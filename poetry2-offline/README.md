## **Build Command**
```bash
docker build -t poetry2-offline -f Dockerfile .
```

## **Pytest Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" poetry2-offline pytest
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" poetry2-offline pytest
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" poetry2-offline pytest
```

## **Pre Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" poetry2-offline pre
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" poetry2-offline pre
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" poetry2-offline pre
```

## **Post Command**

**Windows (Command Prompt):**
```cmd
docker run --rm -v "%CD%:/work" poetry2-offline post
```

**Windows (PowerShell):**
```powershell
docker run --rm -v "${PWD}:/work" poetry2-offline post
```

**Mac/Linux (Bash/Zsh):**
```bash
docker run --rm -v "$(pwd):/work" poetry2-offline post
```
