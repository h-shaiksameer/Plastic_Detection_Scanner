#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef enum {
    TOKEN_IDENTIFIER,
    TOKEN_KEYWORD,
    TOKEN_NUMBER,
    TOKEN_OPERATOR,
    TOKEN_SEPARATOR,
    TOKEN_STRING,
    TOKEN_CHAR,
    TOKEN_UNKNOWN
} TokenType;

typedef struct {
    char lexeme[100];
    TokenType type;
} Token;

char *keywords[] = {"int","float","char","if","else","for","while","return","main","void"};

int isKeyword(char *word) {
    for (int i = 0; i < 10; i++)
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    return 0;
}

int isOperator(char ch) {
    char ops[] = "+-*/=%<>!";
    for (int i = 0; ops[i]; i++)
        if (ch == ops[i])
            return 1;
    return 0;
}

int isSeparator(char ch) {
    char sep[] = "(){},;[]";
    for (int i = 0; sep[i]; i++)
        if (ch == sep[i])
            return 1;
    return 0;
}

int main() {
    char code[1000];
    Token tokens[1000];
    int tcount = 0;

    printf("Enter your C code (end with Ctrl+Z on Windows or Ctrl+D on Linux):\n\n");

    char ch;
    int len = 0;
    while ((ch = getchar()) != EOF) {
        code[len++] = ch;
    }
    code[len] = '\0';

    int i = 0;
    while (i < len) {
        ch = code[i++];

        if (isspace(ch))
            continue;

        if (ch == '/' && code[i] == '/') {
            while (code[i] != '\n' && code[i] != '\0') i++;
            continue;
        }
        if (ch == '/' && code[i] == '*') {
            i++;
            while (code[i] && !(code[i] == '*' && code[i + 1] == '/')) i++;
            i += 2;
            continue;
        }

        if (isalpha(ch) || ch == '_') {
            char word[100];
            int j = 0;
            word[j++] = ch;
            while (isalnum(code[i]) || code[i] == '_')
                word[j++] = code[i++];
            word[j] = '\0';
            tokens[tcount].type = isKeyword(word) ? TOKEN_KEYWORD : TOKEN_IDENTIFIER;
            strcpy(tokens[tcount++].lexeme, word);
        } else if (isdigit(ch)) {
            char num[100];
            int j = 0;
            num[j++] = ch;
            while (isdigit(code[i]) || code[i] == '.')
                num[j++] = code[i++];
            num[j] = '\0';
            tokens[tcount].type = TOKEN_NUMBER;
            strcpy(tokens[tcount++].lexeme, num);
        } else if (ch == '"') {
            char str[200];
            int j = 0;
            str[j++] = ch;
            while (code[i] && code[i] != '"')
                str[j++] = code[i++];
            str[j++] = '"';
            str[j] = '\0';
            i++;
            tokens[tcount].type = TOKEN_STRING;
            strcpy(tokens[tcount++].lexeme, str);
        } else if (ch == '\'') {
            char cval[10];
            int j = 0;
            cval[j++] = ch;
            while (code[i] && code[i] != '\'')
                cval[j++] = code[i++];
            cval[j++] = '\'';
            cval[j] = '\0';
            i++;
            tokens[tcount].type = TOKEN_CHAR;
            strcpy(tokens[tcount++].lexeme, cval);
        } else if (isOperator(ch)) {
            char op[3];
            op[0] = ch;
            if (isOperator(code[i])) {
                op[1] = code[i++];
                op[2] = '\0';
            } else {
                op[1] = '\0';
            }
            tokens[tcount].type = TOKEN_OPERATOR;
            strcpy(tokens[tcount++].lexeme, op);
        } else if (isSeparator(ch)) {
            char sep[2];
            sep[0] = ch;
            sep[1] = '\0';
            tokens[tcount].type = TOKEN_SEPARATOR;
            strcpy(tokens[tcount++].lexeme, sep);
        } else {
            char unk[2];
            unk[0] = ch;
            unk[1] = '\0';
            tokens[tcount].type = TOKEN_UNKNOWN;
            strcpy(tokens[tcount++].lexeme, unk);
        }
    }

    printf("\n---------------------------------\n");
    printf("Lexeme\t\tToken Type\n");
    printf("---------------------------------\n");
    for (int k = 0; k < tcount; k++) {
        char *type_str;
        switch (tokens[k].type) {
            case TOKEN_IDENTIFIER: type_str = "Identifier"; break;
            case TOKEN_KEYWORD: type_str = "Keyword"; break;
            case TOKEN_NUMBER: type_str = "Number"; break;
            case TOKEN_OPERATOR: type_str = "Operator"; break;
            case TOKEN_SEPARATOR: type_str = "Separator"; break;
            case TOKEN_STRING: type_str = "String"; break;
            case TOKEN_CHAR: type_str = "Char"; break;
            default: type_str = "Unknown";
        }
        printf("%-15s %s\n", tokens[k].lexeme, type_str);
    }
    printf("---------------------------------\n");
    return 0;
}
