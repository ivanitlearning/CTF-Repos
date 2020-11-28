/*******************************************
*
*This is an application to print out common log files
*
********************************************/

#include "logMonitor.h"

void printUsage() {
    printf("Usage: %s [-aAbdDfhklmsw] [--help]\n", PROGRAMNAME);
}


int main(int argc, char** argv){
        int opt = 0;
        char filename[26];
        {
                //temporary variables for parsing
                static struct option long_options[] ={
                        /* These options don’t set a flag.
                        We distinguish them by their indices. */
                        {"auth", no_argument, 0, 'a'},
                        {"alternatives", no_argument, 0, 'A'},
                        {"btmp", no_argument, 0, 'b'},
                        {"dpkg", no_argument, 0, 'd'},
                        {"daemon", no_argument, 0, 'D'},
                        {"faillog", no_argument, 0, 'f'},
                        {"help", no_argument, 0, 'h'},
                        {"kern", no_argument, 0, 'k'},
                        {"lastlog", no_argument, 0, 'l'},
                        {"messages", no_argument, 0, 'm'},
                        {"syslog", no_argument, 0, 's'},
                        {"wtmp", no_argument, 0, 'w'},
                        {0,0,0,0}
                };
                //parse the command line arguments
                int option_index = 0;
                while((opt = getopt_long (argc, argv, "aAbdDfhklmsw", long_options, &option_index)) != -1 ){
                        switch (opt) {
                                case 'a' :
                                        strncpy(filename, "/var/log/auth.log", sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'A' :
                                        strncpy(filename, "/var/log/alternatives.log", sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'b' :
                                        strncpy(filename, "/var/log/btmp",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'd' :
                                        strncpy(filename, "/var/log/daemon.log",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'D' :
                                        strncpy(filename, "/var/log/dpkg.log",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'f' :
                                        strncpy(filename, "/var/log/faillog",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'h' :
                                        printUsage();
                                        exit(1);
                                case 'k' :
                                        strncpy(filename, "/var/log/kern.log",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'l' :
                                        strncpy(filename, "/var/log/lastlog",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'm' :
                                        strncpy(filename, "/var/log/messages",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 's' :
                                        strncpy(filename, "/var/log/syslog",sizeof(filename));
                                        printFile(filename);
                                        break;
                                case 'w' :
                                        strncpy(filename, "/var/log/wtmp",sizeof(filename));
                                        printFile(filename);
                                        break;
                                default:
                                        printUsage();
                                        exit(EXIT_FAILURE);
                        }
                }
        }
        return 1;
}