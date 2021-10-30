#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>

//flag
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void* calAverage(void* arguments);//function for calculate the average

struct calArray
{
    int* ArrayInput;
};

void writeFile(int Size);//function for write values in a file

//global variables
float *writeAvg;
int arraySize = 0;
int count = 0;//for write average

int main(void)//main program
{
//Read dataset.txt and take count of rows

    int  d1, d2, d3, d4, d5;//varaibles for store dataset values
    int rowCount = 0; //variable for count rows
    
    FILE *fileRead;
    fileRead = fopen("dataset.txt", "r");
    if (fileRead == NULL)//check the file is opend
    {
       printf("Error opening source file\n");
       perror("Error opening dataset.txt");
       fclose(fileRead);
    }
    else
    {
       fscanf(fileRead, "%d %d %d %d %d", &d1, &d2, &d3, &d4, &d5);
       rowCount++;
       while (!feof(fileRead))
       {
          fscanf(fileRead, "%d %d %d %d %d", &d1, &d2, &d3, &d4, &d5);
          rowCount++;
       }
     
       writeAvg =  calloc(0, sizeof(float));
       arraySize = rowCount;//assigne value to global variable
       fclose(fileRead);
     }

//store data into an array

     int fileArray[rowCount][5];//array for store values

     FILE *fileStore;
     fileStore = fopen("dataset.txt", "r");

     if(fileStore == NULL)
     {
        printf("Error opening sourse file\n");
        perror("Error opening dataset.txt");
        fclose(fileStore);
     }
     else
     {
        for (int c = 0; c < rowCount;c++)
        {
           fscanf(fileStore,"%d %d %d %d %d", &fileArray[c][0],&fileArray[c][1] ,&fileArray[c][2], &fileArray[c][3], &fileArray[c][4]); 
        
       }
       fclose(fileStore);
    }

//print the array
    printf("\n\n*****Values in dataset.txt*****\n");
    for (int c = 0; c < rowCount;c++)
    {
        printf("\t%d\t%d\t%d\t%d\t%d\n", fileArray[c][0], fileArray[c][1], fileArray[c][2], fileArray[c][3], fileArray[c][4]);
    }

//assign structure value
    struct calArray ar1;
    //ar1.size = 5;
    ar1.ArrayInput = calloc(0, sizeof(int));

//thread
    printf("\n\n*****Calculate the average*****\n");
    pthread_t avgThread[rowCount];
    //r = row count c = column count
    for(int r = 0; r < rowCount; r++)
    {
        
        for (int c = 0; c < 5; c++)
        {
            ar1.ArrayInput[c] = fileArray[r][c];//assigne value to ArrayInput;
        }
        //create thread
        if(fileArray[r][0] != 0)
        {
            count = r;
            pthread_create(&avgThread[r], NULL, calAverage, &ar1);
            pthread_join(avgThread[r], NULL);
        }
    } 

    pthread_mutex_destroy(&lock);
 
    //call write function
    printf("\n\n*****Write the results in average.txt*****\n");
    writeFile(rowCount);
    return 0;
}
//declare functions

void* calAverage(void* arguments)//Average calcuat function
{
    pthread_mutex_lock(&lock);
    struct calArray *ar2 = arguments;

    int sum = 0;//variable for sum
    float avg = 0;//variable for average

//calculate average
    for(int i = 0; i <= arraySize; i++)
        {
            sum += (ar2 -> ArrayInput[i]);
        }
            avg = sum / arraySize;

//print results
    
    printf("Row %d --> sum is: %d | average is: %.2f\n",count+1, sum, avg);
    writeAvg[count] = avg;

    pthread_mutex_unlock(&lock);
    pthread_exit(0);
}


void writeFile(int Size)//average.txt write function
{
    FILE * fileWrite;
    fileWrite = fopen("average.txt", "w");
    if(!(fileWrite))
    {
       printf("Error opening source file\n");
       perror("Error opening dataset.txt");
       fclose(fileWrite);
    }
    else
    {
        int counter = 0; //variable for while counter
        while (counter < Size)
        {
            fprintf(fileWrite,"%.2f\n", writeAvg[counter]);
            printf("Result Written :  %.2f\n", writeAvg[counter]);

            counter++;
            
        }
         fclose(fileWrite);
    }  
}
