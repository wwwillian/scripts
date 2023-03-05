#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netdb.h>

int main(int argc, char *argv[])
{
    char *alvo;
    alvo = argv[1];
    
    struct hostent *host;

    char *result;
    char txt[50];
    FILE *rato;
    
    rato = fopen(argv[2], "r");

    if (argc < 2)
    {
        printf("/******************************************************************************************************************************/\n");
        printf("/**********************************                WWWILLIAN | SECURITY-DNS                  **********************************/\n");
        printf("/*****************************                 Willian G. | contato@wwwillian.com                  ****************************/\n");
        printf("/******************************************************************************************************************************/\n\n");

        return 0;
    }

    while (fscanf(rato, "%s", &txt) != EOF)
    {
        result = (char *) strcat(txt,alvo);
        host = gethostbyname(result);
        
        if (host == NULL)
        {
            continue;
        }
      
        printf("HOST ENCONTRADO: %s ===> IP: %s \n", result, inet_ntoa(*((struct in_addr *) host->h_addr_list)));
    }

    fclose(rato);

    return 0;
}
