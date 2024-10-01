# include <stdio.h>
# include <string.h>

int isAllowedUser(char *username) {
  const char *allowedUser[] = "goofy";

  if (strcmp(username, allowedUser) == 0) {
    return 1;
  }
  return 0;
}

void PrivilegedAction() {
  printf("This is a privileged user action.\n");
}

int main () {
  char username[8];
  int allow = 0;

  printf("Enter your username, please: ");
  // gets(username);
  
  fgets(username, sizeof(username), stdin);
  username[strcspn(username, "\n")] = 0;

  if (isAllowedUser(username)) {
    allow = 1;
  }

  if (allow) {
    PrivilegedAction();
  }

  return 0;
}
