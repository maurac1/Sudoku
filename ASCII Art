/***************************************************** 
 ** File: proj1.cpp
 ** Author: Maura Choudhary
 ** Date: 2/17/19
 ** Section: 4
 ** E-mail: maurac1@umbc.edu
 ** Description: This program allows the user to 
 ** create, display, and alter ASCII art.
 ****************************************************/

//libraries

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

//constants

//number of rows in array
const int XSIZE = 75;
//number of columns in the array
const int YSIZE = 75;
//tells the switch to call loadArt function
const int LOAD = 1;
//tells the switch to call createArt function
const int CREATE = 2;
//tells the switch to call displayArt function
const int DISPLAY = 3;
//tells the switch to call rotateArt function
const int ROTATE = 4;
//tells the switch to call invertArt funcion
const int INVERT = 5;
//tells the switch to exit the program
const int EXIT = 6;

//function prototypes

//----------------------------------------------------------------------          
// int displayMenu()                                                              
// Preconditions: none                                                            
// Postconditions: display the menu of options, return the users choice          
//---------------------------------------------------------------------- 
int displayMenu();

//----------------------------------------------------------------                
// void loadArt(char pic[][])                                                     
// Preconditions: an array of the current picture                                 
// Postconditions: load the picture from a file to the array                      
//----------------------------------------------------------------                
void loadArt(char pic[XSIZE][YSIZE]);

//--------------------------------------------------------------                  
// void displayArt(char pic[75][75])                                              
// Preconditions: a character array representing the image                        
// Postconditions: print the image to the console                                 
//--------------------------------------------------------------                  
void displayArt(char pic[XSIZE][YSIZE]);

//----------------------------------------------------------------                
// void createArt(char pic[XSIZE][YZISE])                                         
// Preconditions: a character array representing the image                        
// Postconditions: alter the current image according to user input                
//----------------------------------------------------------------                
void createArt(char pic[XSIZE][YSIZE]);

//-------------------------------------------------------                         
// rotateArt(char pic[XSIZE][YSIZE])                                              
// Preconditions: an array representing the current image                         
// Postconditions: rotate the art in the array 90 degrees                         
//-------------------------------------------------------             
void rotateArt(char pic[XSIZE][YSIZE]);

//-----------------------------------------------------------                     
// invertArt(char pic[XSIZE][YSIZE])                                              
// Preconditions: an array representing the current image                         
// Postconditions: invert the art horizontally or vertically                      
// according to user input                                                        
//-----------------------------------------------------------                     
void invertArt(char pic[XSIZE][YSIZE]);

//--------------------------------------------------------------------            
// vertInvert(char pic[XSIZE][YSIZE])                                             
// Preconditions: an array representing the current image                         
// Postconditions: invert the art vertically, aka rotate the art twice            
//--------------------------------------------------------------------       
void vertInvert(char pic[XSIZE][YSIZE]);

//-------------------------------------------------------                         
// horizInvert(char pic[XSIZE][YSIZE])                                            
// Preconditions: an array representing the current image                         
// Postconditions: invert the art horizontally                                    
//--------------------------------------------------------      
void horizInvert(char pic[XSIZE][YSIZE]);

//main
int main(){
  
  //declare and initialize the array for the image
  char currentPic[XSIZE][YSIZE];
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      currentPic[i][j] = ' ';
    }
  }
  
  int ans = 0;
  
  cout << "Welcome to the ASCII Art Tool" << endl;

  do {

    //display the menu until the user quits 
    ans = displayMenu();

    switch (ans)
    {
    case LOAD:
      //load an image
      loadArt(currentPic);
      break;
    case CREATE:
      //create or edit the current image
      createArt(currentPic);
      break;
    case DISPLAY:
      //display the art to the console
      displayArt(currentPic);
      break;
    case ROTATE:
      //rotate the art 90 degrees
      rotateArt(currentPic);
      break;
    case INVERT:
      //invert the art horizontally or vertically
      invertArt(currentPic);
      break;
    case EXIT:
      //exit the program
      cout << "Goodbye!" << endl;
      break;
    default:
      cout << "Please enter a number 1-5" << endl;
      break;

    }
  }
  while (ans != EXIT);

  return 0;
  
}

//---------------------------------------------------------------------- 
// int displayMenu()
// Preconditions: none
// Postconditions: display the menu of options, return the users choice
//----------------------------------------------------------------------
int displayMenu(){

  cout << "What would you like to do?" << endl
       << "1. Load ASCII Art from File" << endl
       << "2. Create ASCII Art Manually" << endl
       << "3. Display Art" << endl
       << "4. Rotate Art" << endl
       << "5. Invert Art" << endl
       << "6. Exit" << endl;

  //get user input
  int ans = 0;
  cin >> ans;
  return ans;
}

//----------------------------------------------------------------
// void loadArt(char pic[][])
// Preconditions: an array of the current picture
// Postconditions: load the picture from a file to the array
//----------------------------------------------------------------
void loadArt(char pic[XSIZE][YSIZE]){

  //initialize variables
  int xValue;
  int yValue;
  char symbol;
  char fName[80];
  
  if (cin.peek() == '\n')
    cin.ignore();
  cout << "What is the name of the file you would like to input?"<< endl;
  cin.getline(fName, 80);

  //open and read the file into the array
  ifstream myfile(fName);
  if (myfile.is_open()){

    while(myfile >> xValue){
      myfile >> yValue >> symbol;
      pic[xValue][yValue] = symbol;
    }
    
  }else {
    cout << "Unable to open file" << endl;
  }
  myfile.close();
}

//--------------------------------------------------------------
// void displayArt(char pic[75][75])
// Preconditions: a character array representing the image
// Postconditions: print the image to the console
//--------------------------------------------------------------
void displayArt(char pic[XSIZE][YSIZE]){

  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      cout << pic[i][j];
    }
    cout << endl;
  }
}

//----------------------------------------------------------------
// void createArt(char pic[XSIZE][YZISE])
// Preconditions: a character array representing the image
// Postconditions: alter the current image according to user input
//----------------------------------------------------------------
void createArt(char pic[XSIZE][YSIZE]){

  //declare variables
  int xValue;
  int yValue;
  char symbol;

  
  cout << "This will modify the current art" << endl;
  cout << "Enter the x coordinate between 0 and 75" << endl;
  cin >> xValue;

  //validate user input
  while ((xValue < 0) or (xValue > 74)){
    cout << "Enter a value between 0 and 75" << endl;
    cin >> xValue;
  }
  
  cout << "Enter the y coordinate between 0 and 75" << endl;
  cin >> yValue;
  
  //validate user input
  while ((yValue < 0) or (yValue > 74)){
    cout << "Enter a value between 0 and 75" << endl;
    cin >> yValue;
  }
  cout << "Enter the character for that location:" << endl;
  cin >> symbol;

  //alter the image at the corrrect place
  pic[xValue][yValue] = symbol;

}

//-------------------------------------------------------
// rotateArt(char pic[XSIZE][YSIZE])
// Preconditions: an array representing the current image
// Postconditions: rotate the art in the array 90 degrees
//-------------------------------------------------------
void rotateArt(char pic[XSIZE][YSIZE]){

  //create and initialize temporary array
  char tempPic[XSIZE][YSIZE];
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      tempPic[i][j] = ' ';
    }
  }

  //loop through the image and set the values to
  //a different position in the temporary array
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      tempPic[j][(XSIZE - 1)-i] = pic[i][j];
    }
  }

  //update to match the temporary array
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      pic[i][j] = tempPic[i][j];
    }
  }
}

//-----------------------------------------------------------
// invertArt(char pic[XSIZE][YSIZE])
// Preconditions: an array representing the current image
// Postconditions: invert the art horizontally or vertically
// according to user input
//-----------------------------------------------------------
void invertArt(char pic[XSIZE][YSIZE]){

  cout << "Would you like to invert it horizontally or vertically?"
       << endl << "1. Vertical" << endl << "2. Horizontal" << endl;
  int ans;
  cin >> ans;
  
  //validate user input
  while ((ans < 1) or (ans > 2)){
    cout << "Please enter a number 1-2." << endl;
    cin >> ans;
  }

  //call the appropriate inversion function
  if (ans == 1){
    vertInvert(pic);
  }else if (ans == 2){
    horizInvert(pic);
  }
}

//--------------------------------------------------------------------
// vertInvert(char pic[XSIZE][YSIZE])
// Preconditions: an array representing the current image
// Postconditions: invert the art vertically, aka rotate the art twice
//--------------------------------------------------------------------
void vertInvert(char pic[XSIZE][YSIZE]){

  //rotate the art twice
  rotateArt(pic);
  rotateArt(pic);
}

//-------------------------------------------------------
// horizInvert(char pic[XSIZE][YSIZE])
// Preconditions: an array representing the current image
// Postconditions: invert the art horizontally
//--------------------------------------------------------
void horizInvert(char pic[XSIZE][YSIZE]){

  //create and initialize a temporary array
  char tempPic[XSIZE][YSIZE];
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      tempPic[i][j] = ' ';
    }
  }

  //loop through characters and move them in temporary array
  int middleIndex = (XSIZE - 1) / 2;
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < middleIndex; j++){
      tempPic[i][(YSIZE-1)-j] = pic[i][j];
    }
  }

  //left side reflection
  for(int i = 0; i < XSIZE; i++){
    for(int j = (middleIndex + 1); j < YSIZE; j++){
      tempPic[i][(YSIZE-1) -j] = pic[i][j];
    }
  }

  //middle column
  for(int i = 0; i < XSIZE; i++){
    tempPic[i][middleIndex] = pic[i][middleIndex];
  }
  
  //right side reflection
  for (int i = 0; i < XSIZE; i++){
    for (int j = 0; j < YSIZE; j++){
      pic[i][j] = tempPic[i][j];
    }
  }
}
