# Task

1. Create a ReST-API for generating password and keeping track of the generated passwords, based on the user requirements.
2. The app will have 2 endpoints,
  A. GetPassword (Generate a new password)
   Payload: 
```
{
    "lenght":<int>[6,16],
    "useSpecialChars":<int>[0,1],
    "useNumbers":<int>[0,1], 
    "useCapitalLetters":<int>[0,1]
}
```
  B. IsUsedPassword (Is the given password already used)
   Payload:'{"password":<string>}'
 
## Requirements for the ReST-API.

1. Use any of the tools (FastAPI, Flask or Django)
2. Use data validation modules such as (Pydantic, dataclasses, atters etc....)
3. Store the generated password locally.
4. Check the local collection against the given password.
5. Use class based approach instead of simple functions.
6. Use decorators when possible.
7. Create a Git Repository and push the code to the repository.
