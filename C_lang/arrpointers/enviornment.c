/* For I/O like printf, puts  */
#include <stdio.h>
/* For datatype size_t and function of strings like strlen */
#include <string.h>
/* For NULL and exit macros */
#include <stdlib.h>

char** CopyEnv ()
{
    extern char **environ;
    char **buffer;
    char *envVar, *cpyEnvVar;
    int numOfEnv, i, j;

    for (numOfEnv=0; environ[numOfEnv] != NULL; numOfEnv++) {}

    buffer = malloc((numOfEnv+1) * sizeof(char*));
    if (buffer == NULL)
    {
        puts("Memory allocation failed.");
        exit (1);
    }

    for (i=0; environ[i] != NULL; i++)
    {
        envVar = environ[i];
        cpyEnvVar = malloc(strlen(envVar)+1);
        if (cpyEnvVar == NULL)
        {
            for (j=0; j<i; j++)
            {
                free(buffer[j]);
            }
            free(buffer);
            puts("Memory allocation failed.");
            exit (1);
        }
        strcpy(cpyEnvVar, envVar);
        buffer[i] = cpyEnvVar;
    }
    buffer[numOfEnv] = NULL;

    return buffer;
}

void ToLower (char **env)
{
    int i, j;
    for (i=0; env[i] != NULL; i++)
    {
        for (j=0; env[i][j] != '\0'; j++)
        {
            env[i][j] = tolower(env[i][j]);
        }
    }
}

int main()
{
    char **env_copy = CopyEnv();
    int i;
    
    if (env_copy == NULL)
    {
        puts("Copying environment variables failed.");
        return 1;
    }

    ToLower(env_copy);

    for (i=0; env_copy[i] != NULL; i++)
    {
        printf("%s\n", env_copy[i]);
        free(env_copy[i]);
    }
    free(env_copy);

    return 0;
}

/* Shorter solution without **buffer

int main()
{
   extern char **environ;
   char *env, *lower_env;
   int i,j;

   for (i=0; environ[i] != NULL; i++)
   {
      env = environ[i];
      lower_env = malloc(strlen(env)+1);

      if (lower_env == NULL)
      {
         puts("Memory allocation failed.");
         exit (1);
      }

      for (j=0; env[j]; j++)
      {
         lower_env[j] = tolower(env[j]);
      }

      lower_env[strlen(env)] = '\0';
      printf("%s\n", lower_env);
      free(lower_env);
   }

   return 0;
}
*/
