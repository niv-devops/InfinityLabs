#include <stdio.h> /* For I/O like printf, gets etc.  */
#include <string.h> /* For datatype size_t and function of strings like strlen */
#include <stdlib.h> /* For NULL and exit macros */

FILE *fptr;

typedef enum 
{
	ERR_FIND_FILE = 0,
	ERR_OPEN_FILE,
	ERR_DELETE,
	ERR_PREPEND,
	ERROR,
	SUCC_DELETE,
	SUCC_EXIT,
	SUCC_PREPEND,
	SUCCESS
} OpsReturn;

const char *opsReturnMsg[] = {
    "File name not specified.",
    "Could not open file.",
    "Error deleting file.",
    "Error prepending text.",
    "Error writing to file.",
    "File deleted successfully.",
    "Exiting...",
    "Text prepend to file.",
    "Operation executed successfuly."
};

typedef struct command
{
	const char *cmd;
	int (*comp)(const char *, const char *);
	OpsReturn (*opt)(const char*, const char *);
} command;

int Compare (const char *cmd, const char *text);
OpsReturn Remove (const char *filename, const char *text);
OpsReturn Count(const char *filename, const char *text);
OpsReturn Exit(const char *filename, const char *text);
OpsReturn Prepend(const char *filename, const char *text);
OpsReturn Write(const char *filename, const char *text);

int main(int argc, char * argv[]) 
{
	char *filename = argv[1];
	char text[80];
	int numCommands, i;
	size_t length;
	OpsReturn result;
	
	struct command commands[] = {
		{"-remove", Compare, Remove},
		{"-count", Compare, Count},
		{"-exit", Compare, Exit},
		{"<", Compare, Prepend},
		{"str", Compare, Write}   
	};
   
	numCommands = sizeof(commands) / sizeof(commands[0]);
	
	if (NULL == argv[1] && argc<2)
	{
		printf("%s\n", opsReturnMsg[ERR_FIND_FILE]);
		return ERR_FIND_FILE;
	}
   
	puts("Enter some text: ");
	while (1)
	{
		fgets(text, sizeof(text), stdin);
		length = strlen(text)-1;
      
		while (!strchr(text, '\n'))
		{
			puts("Max size is 80 chars. Enter another text: ");
			fgets(text, sizeof(text), stdin);
			length = strlen(text)-1;
		}
      
		if ('\n' == text[length])
		{
			text[length] = '\0';
		}

		for (i=0; i<numCommands; i++)
		{
			if (commands[i].comp(commands[i].cmd, text))
			{
				result = commands[i].opt(filename, text);
				if (ERROR == result)
				{
					return ERROR;
				}
				break;
			}
			if (numCommands-1 == i)
			{
				result = commands[i].opt(filename, text);
				if (ERROR == result)
				{
					return ERROR;
				}
				break;
			}

			if (2 == commands[i].comp(commands[i].cmd, text))
			{
				result = commands[3].opt(filename, text);
				if (ERROR == result)
				{
					return ERROR;
				}
				break;
			}
		}
	}
	return SUCCESS;
}

int Compare (const char *cmd, const char *text) 
{
	if (text[0] == '<' && cmd[0] == '<')
	{
		return 2;   
	}
	return (strcmp(cmd, text) == 0);
}

OpsReturn Remove (const char *filename, const char *text)
{
	fptr = fopen(filename, "a");
	(void) text;
	if (NULL == fptr)
	{
		printf("%s\n", opsReturnMsg[ERR_OPEN_FILE]);
		return ERR_OPEN_FILE;
	}
	if (remove(filename) == 0)
	{
		printf("%s\n", opsReturnMsg[SUCC_DELETE]);
		return SUCC_DELETE;
	}
	else
	{
		printf("%s\n", opsReturnMsg[ERR_DELETE]);
		return ERR_DELETE;
	}
	fclose(fptr);
}

OpsReturn Count(const char *filename, const char *text)
{
	int lines=0, c;
	fptr = fopen(filename, "r");
	(void) text;
	if (NULL == fptr)
	{
		printf("%s\n", opsReturnMsg[ERR_OPEN_FILE]);
		return ERR_OPEN_FILE;
	}
	for (c = getc(fptr); c != EOF; c = getc(fptr))
	{
		if ('\n' == c)
		{
			++lines;
		}
	}
	printf("Number of lines in file: %d\n", lines);
	fclose(fptr);
	return SUCCESS;
}

OpsReturn Exit(const char *filename, const char *text)
{
	(void) filename;
	(void) text;
	printf("%s\n", opsReturnMsg[SUCC_EXIT]);
	exit (0);
	return SUCC_EXIT;
}

OpsReturn Prepend(const char *filename, const char *text)
{
	size_t readBytes = 0;
	char buffer[80];
	fopen(filename, "r+");
	readBytes = fread(buffer, 1, sizeof(buffer), fptr);
   
	if(0 == readBytes)
	{
		fclose(fptr);
		printf("%s\n", opsReturnMsg[ERR_FIND_FILE]);
		return ERROR;
	}
   
	++text;
	fseek(fptr, 0, SEEK_SET);
	fwrite(text, 1, strlen(text), fptr);
	fputs("\n", fptr);
	fwrite(buffer, 1, readBytes, fptr);
	fclose(fptr);
	printf("%s\n", opsReturnMsg[SUCC_PREPEND]);
	return SUCC_PREPEND;
}

OpsReturn Write(const char *filename, const char *text)
{
	fptr = fopen(filename, "a");
	if (NULL == fptr)
	{
		printf("%s\n", opsReturnMsg[ERR_OPEN_FILE]);
		return ERR_OPEN_FILE;
	}
	fputs(text, fptr);
	fputs("\n", fptr);
	fclose(fptr);
	return SUCCESS;
}
