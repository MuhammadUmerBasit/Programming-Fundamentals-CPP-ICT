/**
002
 
003
*/
#include <stdio.h> // Standard Input/Output Library use f or printf() and scanf() functions.
#include <stdlib.h> // Standard Library - Used for system() function.
#include <string.h>
#include <time.h>
 
// Define Constants //
#define MAXSONGREC 100
#define MAXLENGTH 40
 
////////////////////////////////////////////////////////////////////
/////////////////// Structures /////////////////////////////////////
////////////////////////////////////////////////////////////////////
static struct
{
    char title[MAXLENGTH];
    char artist[MAXLENGTH];
    char genre[MAXLENGTH];
    int year;
    float time;
    char fileLocation[MAXLENGTH];
} trackInfo[MAXSONGREC];

////////////////////////////////////////////////////////////////////
//////////////////***Prototypes--Function***////////////////////////
////////////////////////////////////////////////////////////////////
 
int trakOption(void);
 
////////////////////////////////////////////////////////////////////
////////////////////////**** Main Function ****//////////////////////
////////////////////////////////////////////////////////////////////
int main(void)
{
      int arrayTrack = 0, position = 0, menuchoice = 0; // Declare and Initilise Variables.
      FILE *fp;     
       
      fp = fopen("trackDetails.text", "rt");           // open a file where stored the Song record
       
      if(fp == NULL)
      {
           printf("\nUnable to open Database. May not found or corrupted.\n");
           exit(EXIT_FAILURE);
      }
      else
      {

           fscanf(fp, "%d\n", &arrayTrack);
            
           // printf("%d\n", arrayTrack size);
           for(position = 0; position < arrayTrack; position++)
           {
                fgets(trackInfo[position].title, sizeof(trackInfo[position].title), fp);
                fgets(trackInfo[position].artist, sizeof(trackInfo[position].artist), fp);
                fgets(trackInfo[position].genre, sizeof(trackInfo[position].genre), fp);
                fscanf(fp, "%d\n", &trackInfo[position].year);
                fscanf(fp, "%f\n", &trackInfo[position].time);
                fgets(trackInfo[position].fileLocation, sizeof(trackInfo[position].fileLocation), fp);
           }
            
           while(menuchoice != 6) // Another loop to run the program until quit.
           {
                 printf("\nWELCOME TO RUSKIN-POD MP3 PLAYER :\n");
                 printf("\n==================================\n");
                 printf("\n1. Track Option:");
                 printf("\n2. Current Track list to a disk File : ");
                 printf("\n3. Display all track and current Track : ");
                 printf("\n4. Space free percent : ");
                 printf("\n5. Create playlist by selcting number : ");
                 printf("\n6. End Program");
                  
                 printf("\n\n");
                  

                 scanf("%d", &menuchoice);

                  

                 switch(menuchoice)              

                 {

                        case 1:

                            printf("\nTrack Option : \n");

                            printf("\nYou select Track option :");

                            printf("\n=========================\n");

                             

                            int choice; int nb_song; int song_nb;

                            int arrayTrack;                          

                             

                            while(choice != 4)

                            

                                    printf("\n1. Add Track: ");

                                    if(nb_song < MAXSONGREC)

                                    {

                                               printf("\nEnter Song number: ");

                                               scanf("%d", &nb_song);

                                               int arrayTrack[nb_song] = {song_nb};

                                               nb_song= nb_song + 1; // or nb_song++

                                                

                                                

                                                

                                                

                                    }

                                    else

                                    {

                                              printf("\nSorry, The MP3 Pod is Full.");

                                    }             

                             

                            break;

                        case 2:

                            printf("\n2. Current Track list to a disk File : ");

                            printf("\n=====================================\n");

                        // Invoke Playlist Manager Function

                            printf("Song: %s\n", trackInfo[1].title);

                            break;

                        case 3:

                            printf("\n3. Display all track and current Track : ");

                        // Display Info track list which is recorded in database

                            int arraytrack;

             

                            for(position = 0; position < arraytrack; position++)

                            {

                                    printf("%s", trackInfo[position].title);

                                    printf("%s", trackInfo[position].artist);

                                    printf("%s", trackInfo[position].genre);

                                    printf("%d", trackInfo[position].year);

                                    printf("\n%f", trackInfo[position].time);

                                    printf("\n%s\n", trackInfo[position].fileLocation);

                            }

                        case 4:

                            printf("\n4. Space free percent : ");

                            printf("\n======================\n");

                              

                            break;

                        case 5:

                            printf("\n5. Create playlist by selcting number : ");

                            printf("\n=====================================\n");

                              

                            break;

                        case 6:                     

                            printf("\nTHANK YOU FOR PLAYING RUSKIN POD MP3 PLAYER. GOOD BYE.\n\n");

                            break;

                        default:

                            printf("\nInvalid choice. Please repeat your choice again 1 to 4");

                            printf("\n========================================================\n");

                            break;

                 }

           }

      }

      fclose(fp);

       

      printf("\n\n");

      system("pause");

       

      return 0;

}

 

////////////////////////////////////////////////////////////////////

////////////////// User-Defined Functions //////////////////////////

////////////////////////////////////////////////////////////////////

////////////////// Track delete Function ///////////////////////////

 

int trackOption(void)

{

    int trackChoice = 0, deleteTrack=0, position;

     

    while(trackChoice != 5)

    {

            printf("\nTrack Option Activity. Please choose your option: \n");

            printf("\n1. Add Track to Database : ");

            printf("\n2. Delete Track From Database");

            printf("\n3. Play Individual Track");

            printf("\n5. Return to Main Program");

            printf("\n=========================\n");

             

            scanf("%d", &trackChoice);

 

            switch(trackChoice)

            {

            case 1:

            // Code to Add Track

            case 2:

            // Code to Play Track

            case 3:

            // Code to Delete Track

            case 4:

                  

            printf("\nDISPLAY ALL TRACK RECORDED IN DATABASE\n");

            printf("\n=========================================\n");

            int arraytrack;

             

            for(position = 0; position < arraytrack; position++)

            {

                    printf("%s", trackInfo[position].title);

                    printf("%s", trackInfo[position].artist);

                    printf("%s", trackInfo[position].genre);

                    printf("%d", trackInfo[position].year);

                    printf("\n%f", trackInfo[position].time);

                    printf("\n%s\n", trackInfo[position].fileLocation);

            }

             

            break;

            case 5:

            printf("\nExiting Track Option.");

            break;

            default:

            printf("\nReturn to Main function. Please select a number from 1 to 5.");

            break;

            }

    }

     

    system("pause");
}


