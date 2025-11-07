%{
#include <stdio.h>
int line_count = 0;
%}

DIGIT       [0-9]
ID          [a-zA-Z_][a-zA-Z0-9_]*
OP          [+\-*/=<>]
SEP         [(){},;]

%%

[ \t]+              ;                      /* ignore spaces and tabs */
\n                  { line_count++; }      /* count new lines */
{ID}                { printf("%-15s Identifier\n", yytext); }
{DIGIT}+            { printf("%-15s Number\n", yytext); }
{OP}                { printf("%-15s Operator\n", yytext); }
{SEP}               { printf("%-15s Separator\n", yytext); }
.                   { printf("%-15s Unknown\n", yytext); }

%%

int yywrap() { return 1; }

int main() {
    printf("-----------------------------------\n");
    printf("Lexeme\t\tToken Type\n");
    printf("-----------------------------------\n");
    yylex();
    printf("-----------------------------------\n");
    printf("Total lines: %d\n", line_count);
    return 0;
}
