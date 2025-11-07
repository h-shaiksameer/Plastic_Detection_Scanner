%{
#include <stdio.h>
int word_count = 0;
int line_count = 0;
FILE *fp;
%}

WORD        [a-zA-Z]+
NEWLINE     \n

%%

{WORD}      { word_count++; }
{NEWLINE}   { line_count++; }
.           { /* ignore other characters */ }

%%

int yywrap() { return 1; }

int main() {
    char filename[100];
    printf("Enter the file name: ");
    scanf("%s", filename);

    fp = fopen(filename, "r");
    if (!fp) {
        printf("Error: Could not open file %s\n", filename);
        return 1;
    }

    yyin = fp;   // Tell Lex to read from this file
    yylex();

    printf("\nTotal Words: %d\n", word_count);
    printf("Total Lines: %d\n", line_count);

    fclose(fp);
    return 0;
}
