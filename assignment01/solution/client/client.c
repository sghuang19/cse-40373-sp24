#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define ZMQ_SERVER_PORT 40226
#define BEACON_NAME_LEN 18

int main (void)
{
    int rc;             /* Save the return code */

    printf ("Connecting to server on port %d ... \n", ZMQ_SERVER_PORT);
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);

    char pszRequest[25];
    sprintf(pszRequest, "tcp://localhost:%d", ZMQ_SERVER_PORT);

    rc = zmq_connect (requester, pszRequest);

    if(rc == 0)
    {
        /* If this printf is printed, the network is working */
        printf("  Successfully connected on port %d\n", ZMQ_SERVER_PORT);
    }
    else 
    {
        printf("  Network connection failed\n");
        exit(-1);
    }

    printf("Usage: Input a beacon name and press enter to query its info,\n");
    printf("       enter 'exit' to terminate the client.\n");

    char buffer[BUFSIZ];

    while (1) {
	memset(buffer, 0, BUFSIZ);
	fgets(buffer, BUFSIZ, stdin);
	if (strcmp(buffer, "exit\n") == 0) {
	    exit(0);
	    printf("Exiting client");
	}
        zmq_send (requester, buffer, strlen(buffer), 0);

        memset(buffer, 0, BUFSIZ);
        zmq_recv (requester, buffer, BUFSIZ, 0);
        printf ("%s\n", buffer);
    }

    zmq_close (requester);
    zmq_ctx_destroy (context);
    return 0;
}
