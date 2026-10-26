#include<iostream>
#include<string>
#include<windows.h>
using namespace std;

void intro();
void display();
void closedisplay();
void tryagain();
void load();
int findrollno(int);
int checkchoice(string);

int main()
{
	int rollno[25],rl=11601,id[25],d=1;
	for(int i=1;i<=25;i++)
	{
		rollno[i]=rl;
		rl++;               // for roll no increment
		id[i]=d;
		d++;				// for id increment
	}
	
	intro();
	struct student
	{
		float m,per;
		string name,cnic,email,ch1,ch2,ch3,password,dept;
	};
	student rec[25];
	int i=1,ch,idi;

	start:
	display();
	cin>>ch;
	switch(ch)    
	{
	    case 1:
		    {
		        system("cls");
		        cout<<"\t\t\t\t************************************************"<<endl;
		        cout<<"\t\t\t\t*              Register Here                   *"<<endl;
		        cout<<"\t\t\t\t************************************************"<<endl;

		    	cout<<"\nID:UG-19-"<<id[i]<<endl;
		    	cout<<"\nRoll No:"<<rollno[i]<<endl;
				cin.ignore();               //Removes unwanted left character which may cause skipping in getline function

				rename:
		        cout<<"\nEnter Name:";
		        getline(cin,rec[i].name);
		        if(rec[i].name.length()==0)
		        goto rename;

		        wcnic:
		        cout<<"\nEnter CNIC:";
		        getline(cin,rec[i].cnic);
		        if(rec[i].cnic.length()!=13)       //Checks Length of cnic if not 13 retakes input
		        goto wcnic;

		        cout<<"\nEnter Email:";
		        getline(cin,rec[i].email);

				repassword:
		        cout<<"\nEnter Password of 7 Chars:";
		        getline(cin,rec[i].password);
		        if(rec[i].password.length()!=7)		//Checks Length of password if not 7 retakes input
		        goto repassword;

		        wc:
		        cout<<"\nWrite ME,EE,CE in capitals only\n";
				cout<<"Enter Choice 1:";
		        getline(cin,rec[i].ch1);
				ch=checkchoice(rec[i].ch1);            //Checks if choice no 1 is either CE, EE, ME returns 0 if condition not met else 1
		        if(ch==0)
		        goto wc;

		        cout<<"Enter Choice 2:";
		        getline(cin,rec[i].ch2);
		        ch=checkchoice(rec[i].ch2);            //Checks if choice no 2 is either CE, EE, ME returns 0 if condition not met else 1
		        if(ch==0)
		        goto wc;

		        cout<<"Enter Choice 3:";
		        getline(cin,rec[i].ch3);
		        ch=checkchoice(rec[i].ch3);            //Checks if choice no 3 is either CE, EE, ME returns 0 if condition not met else 1
		        if(ch==0)
		        goto wc;

				i++;
				cout<<"\n\n\n1-Menu";
		        cout<<"\n2-Exit";
		        cout<<"\nEnter Choice:";
		        cin>>ch;
		        if(ch==1)
		        goto start;
		        else
		        goto exit;
		        break;
		    }

	    case 2:
		    {
		    	//Displaying Registered Students
		        idi=1;
			    system("cls");
		        cout<<"\t\t\t\t************************************************"<<endl;
		        cout<<"\t\t\t\t*              Registered Students             *"<<endl;
		        cout<<"\t\t\t\t************************************************"<<endl;
		        while(idi<=i)
		        {
			        cout<<"\n"<<idi<<"-";
			        cout<<"\tID:UG-19-"<<id[idi];
					cout<<"\tRoll No:"<<rollno[idi];
					cout<<"\tName:"<<rec[idi].name;
					cout<<"\tFirst Choice:"<<rec[idi].ch1;  
		            idi++;
				}        
		        cout<<"\n\n\n1-Menu";
		        cout<<"\n2-Exit";
		        cout<<"\nEnter Choice:";
		        cin>>ch;
		        if(ch==1)
		        goto start;
		        else
		        goto exit;
		        break;
		    }
	
	    case 3:
			{
				//Login And Taking Exam
			    int temprollno,tempid;
		        system("cls");
		        cout<<"\t\t\t\t************************************************"<<endl;
		        cout<<"\t\t\t\t*                      Quiz                    *"<<endl;
		        cout<<"\t\t\t\t************************************************"<<endl;
		        cout<<"\n\nEnter Roll No:";
		        cin>>temprollno;
			    cin.ignore();
				tempid=findrollno(temprollno); 
				if(temprollno==rollno[tempid])
				{
					int tries=0;
			        string temppass,tempname;
			        tryagain:
			    	system("cls");
			    	cout<<"\t\t\t\t************************************************\n";
			    	cout<<"\t\t\t\t*                     Login                    *\n";
			    	cout<<"\t\t\t\t************************************************\n";
			        cout<<"\t\tTries="<<tries;
			        cout<<"\nEnter Name:";
			        getline(cin,tempname);
				    cout<<"\nEnter Password:";
				    getline(cin,temppass);
		
		            if(tempname.compare(rec[tempid].name)==0&&temppass.compare(rec[tempid].password)==0)    
					{
				    	system("cls");
				        load();                  //calling loading on confirm authentication
				    	string engq[4],mathq[4],compq[4],phyq[4];
						char ans1[4],ans2[4],ans3[4],ans4[4],ans;
						int check[11];
				        int j,qs,marks=0;
		
						phyq[1]="What is the unit of velocity? \n (a) cm \t (b) km \n(c) m s^-1 \t (d) m/s^2";
						ans1[1]='c';
				        phyq[2]="How many types of quantities are used in physics? \n (a) three \t (b) five \n (c) six \t (d) two";
				        ans1[2]='d';
			         	phyq[3]="Physics is the study of ? \n (a) matter & energy \t (b) space \n (c) water \t (d) stars & plants";
			         	ans1[3]='a';
				        compq[1]="Which is the pointing device? \n (a) cpu \t (b) mouse \n (c) scanner \t (d) keyboard";
				        ans2[1]='b';
				        compq[2]="IP stand for? \n (a) Internet protocol \t (b) Input power \n (c) Internet process";
				        ans2[2]='a';
				        compq[3]="OCR stand for? \n (a) optical capital reader \t (b) optical character recognition \n (c) optical card reader";
				        ans2[3]='b';
						engq[1]="I am going------- market. \n (a) a \t (b) an \n (c) to \t (d) be";
						ans3[1]='c';
				        engq[2]="Cat is sitting------- the table. \n (a) above \t (b) under \n (c) up \t (d) down";
				        ans3[2]='b';
				        engq[3]="There are------- vowel letters. \n (a) nine \t (b) ten \n (c) five \t (d) three";
				        ans3[3]='c';
			        	mathq[1]="Which one is the fabnoccie series? \n(a) 1+1+2+3+5+8+13+21+------ \t (b) 1+2+3+4+------ \n (c) 0+1+1+2+3+5+8+------ \t (d) 1+3+5+7+9+----- \n";
			        	ans4[1]='a';
			        	mathq[2]="Square root of 225 is? \n (a) 5 \t (b) 10 \n (c) 15 \t (d) 17";
			        	ans4[2]='c';
						mathq[3]="What is the value of pie? \n (a) 3.12 \t (b) 3.15 \n (c) 2.14 \t (d) 3.14";
						ans4[3]='d';
		
			        	for(int i=1;i<=10;i++)
			        	check[i]=0;                       
		
			        	system("cls");
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\t\t\t\t*                 Entry Test                 *\n";
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\n\n\nName:"<<rec[tempid].name<<"\t\tUG-19-"<<id[tempid]<<endl;
			            cout<<"\n\n\t\tPhysics\n\n";
						j=0;
			            phy:
			            qs=rand() % 10 + 1;                //Random Numbers So Every Registered Student Gets Diff Pattern
		
			            while(j!=3)
			            {
			                if(qs<=3)
			                    if(check[qs]==0)           //Check So Same Question Is Not Repeated
			                  	{
		                            cout<<(j+1)<<") "<<phyq[qs]<<endl;
								    cout<<"Enter Choice:";
									cin>>ans;
								    j++;                //Only increments when student answers 
									if(ans1[qs]==tolower(ans))
									marks=marks+5;
									check[qs]=1;
									goto phy;
								}
								else
								    goto phy;
							else
							    goto phy;
						}
				
			        	for(int i=1;i<=10;i++)
			        	check[i]=0;
		
			        	system("cls");
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\t\t\t\t*                 Entry Test                 *\n";
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\n\n\nName:"<<rec[tempid].name<<"\t\tUG-19-"<<id[tempid]<<endl;
			            cout<<"\n\n\t\tComputer\n\n";
						j=0;
			            comp:
			            qs=rand() % 10 + 1;                  //Random Numbers So Every Registered Student Gets Diff Pattern
		
			            while(j!=3)
			            {
			                if(qs<=3)
			                    if(check[qs]==0)              //Check So Same Question Is Not Repeated
		                        {
		                            cout<<(j+1)<<") "<<compq[qs]<<endl;
									cout<<"Enter Choice:";
									cin>>ans;
								    j++;                   //Only increments when student answers
									if(ans2[qs]==tolower(ans))
									marks=marks+5;
									check[qs]=1;
									goto comp;
								}
								else
								    goto comp;
							else
							    goto comp;
						}
		
			        	for(int i=1;i<=10;i++)
			        	check[i]=0;
		
			        	system("cls");
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\t\t\t\t*                 Entry Test                 *\n";
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\n\n\nName:"<<rec[tempid].name<<"\t\tUG-19-"<<id[tempid]<<endl;
			            cout<<"\n\n\t\tEnglish\n\n";
						j=0;
			            eng:
			            qs=rand() % 10 + 1;                //Random Numbers So Every Registered Student Gets Diff Pattern
		
			            while(j!=3)
			            {
			                if(qs<=3)
			                    if(check[qs]==0)           //Check So Same Question Is Not Repeated
			                    {
		                        	cout<<(j+1)<<") "<<engq[qs]<<endl;
								    cout<<"Enter Choice:";
									cin>>ans;
								    j++;                //Only increments when student answers
									if(ans3[qs]==tolower(ans))
									marks=marks+5;
									check[qs]=1;
									goto eng;
								}
								else
								    goto eng;
							else
							    goto eng;
						}
		
			        	for(int i=1;i<=10;i++)
			        	check[i]=0;
			        	system("cls");
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\t\t\t\t*                 Entry Test                 *\n";
			            cout<<"\t\t\t\t**********************************************\n";
			            cout<<"\n\n\nName:"<<rec[tempid].name<<"\t\tUG-19-"<<id[tempid]<<endl;
			            cout<<"\n\n\t\tMathematics\n\n";
						j=0;
			            math:
			            qs=rand() % 10 + 1;                      //Random Numbers So Every Registered Student Gets Diff Pattern
		
			            while(j!=3)
			            {
			                if(qs<=3)
			                    if(check[qs]==0)                 //Check So Same Question Is Not Repeated
		                        {
		                            cout<<endl<<(j+1)<<") "<<mathq[qs]<<endl;
								    cout<<"Enter Choice:";
									cin>>ans;
								    j++;                      //Only increments when student answers
									if(ans4[qs]==tolower(ans))
									marks=marks+5;
									check[qs]=1;
									goto math;
								}
								else
								    goto math;
							else
							    goto math;
						}
		
						rec[tempid].m=marks;
						rec[tempid].per=(rec[tempid].m*100)/60;

						if(rec[tempid].per>=65)
						{
					        system("cls");
							cout<<"You Have Been Admitted To BS ";
		
					        if(rec[tempid].ch1.compare("ME")==0&&rec[tempid].per>=75)
				            {
				               cout<<"ME\n";  
						    }
		
							else if(rec[tempid].ch1.compare("EE")==0&&rec[tempid].per>=70)
				            {
				               cout<<"EE\n"; 
						    }
		
							else if(rec[tempid].ch1.compare("CE")==0&&rec[tempid].per>=65)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[tempid].ch2.compare("ME")==0&&rec[tempid].per>=75)
				            {
				               cout<<"ME\n"; 
						    }
		
							else if(rec[tempid].ch2.compare("EE")==0&&rec[tempid].per>=70)
				            {
				               cout<<"EE\n"; 
						    }
		
							else if(rec[tempid].ch2.compare("CE")==0&&rec[tempid].per>=65)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[tempid].ch3.compare("ME")==0&&rec[tempid].per>=75)
				            {
				               cout<<"ME\n";
						    }
		
						    else if(rec[tempid].ch3.compare("EE")==0&&rec[tempid].per>=70)
				            {
				               cout<<"EE\n";
						    }
		
							else if(rec[tempid].ch3.compare("CE")==0&&rec[tempid].per>=65)
				            {
				               cout<<"CE\n";
						    }
		
			         	//gets department by checking choices and required percentage
		
					    }
						else
					    {
					    	system("cls");
					        cout<<"You Failed The Test\n";
						}
					}
		            else
		            {
						tries++;
						if(tries==5)
					    {   
					        system("cls");
					        tryagain();                          //try again wait for 30 sec on 5 wrong tries
					        tries=tries-5;
						}
						cout<<"\n\nName & Password Doesnt Match\nDo You Want Try Again (Y=Yes) & (N=No)\n";
						char choicelogin;
						cin>>choicelogin;
						cin.ignore();
						if(tolower(choicelogin)=='y')
						goto tryagain;
				 	}
				    cout<<"\n\n1-Main\n2-Exit\nEnter Choice:";
					cin>>ch;
					if(ch==1)
					goto start;
					if(ch==2)
					goto exit;
				}
				else
			    {
				    cout<<"Roll no not found going back to main menu\n";
				    Sleep(2000);
					goto start;
				}
			
			   	break;
			}
	
		case 4:
			{    
		        //Display Result Of All Students
		        system("cls");
		        idi=1;
		        while(idi<=i)
		        { 
			        cout<<"Name:"<<rec[idi].name;
				    cout<<"\tUG-19-"<<id[idi];
				    cout<<"\tMarks:"<<rec[idi].m<<"/60";
				    cout<<"\tPercentage:"<<rec[idi].per<<"%";
		
					if(rec[idi].per>=50)
					{
					    	cout<<"\tAdmitted To BS-";
		
					        if(rec[idi].ch1.compare("ME")==0&&rec[idi].per>=60)
				            {
				               cout<<"ME\n";  
						    }
		
							else if(rec[idi].ch1.compare("CE")==0&&rec[idi].per>=55)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[idi].ch1.compare("EE")==0&&rec[idi].per>=50)
				            {
				               cout<<"EE\n"; 
						    }
		
							else if(rec[idi].ch2.compare("ME")==0&&rec[idi].per>=60)
				            {
				               cout<<"ME\n"; 
						    }
		
							else if(rec[idi].ch2.compare("CE")==0&&rec[idi].per>=55)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[idi].ch2.compare("EE")==0&&rec[idi].per>=50)
				            {
				               cout<<"IT\n"; 
						    }
		
							else if(rec[idi].ch3.compare("ME")==0&&rec[idi].per>=60)
				            {
				               cout<<"ME\n";
						    }
		
						    else if(rec[idi].ch3.compare("CE")==0&&rec[idi].per>=55)
				            {
				               cout<<"CE\n";
						    }
		
							else if(rec[idi].ch3.compare("EE")==0&&rec[idi].per>=50)
				            {
				               cout<<"EE\n";
						    }                                                             
		                                                             
		             }
					else
				         {
				    	cout<<"\tFailed\n";
					       }
				    	idi++; 
			                             
		                           	}
		
				cout<<"\n\n1-Main\n2-Exit\nEnter Choice:";
		        cin>>ch;
				if(ch==1)
				goto start;
				if(ch==2)
				goto exit;
				break;
			}
	
		case 5:
		   	{    
		        //Display Result Of Student Only Whose Roll No Is Entered
		        int rn;
		        system("cls");
		        cout<<"Enter Roll No:";
		        cin>>rn;
		        int temid=findrollno(rn);		
				if(rn==rollno[temid])
			    {
			    	system("cls");
					cout<<"Waiting";
			    	Sleep(1000);
				    for(int i=1;i<6;i++)
			        {
			            cout<<".";
			            Sleep(600);
			        }
				    system("cls");
					cout<<"Name:"<<rec[temid].name;
				    cout<<"\tUG-19-"<<id[temid];
				    cout<<"\tMarks:"<<rec[temid].m<<"/60";
				    cout<<"\tPercentage:"<<rec[temid].per<<"%";
		
					if(rec[temid].per>=50)
				    {
							cout<<"\tAdmitted To BS-";
		
					        if(rec[temid].ch1.compare("ME")==0&&rec[temid].per>=60)
				            {
				               cout<<"ME\n";  
						    }
		
							else if(rec[temid].ch1.compare("CE")==0&&rec[temid].per>=55)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[temid].ch1.compare("EE")==0&&rec[temid].per>=50)
				            {
				               cout<<"EE\n"; 
						    }
		
							else if(rec[temid].ch2.compare("ME")==0&&rec[temid].per>=60)
				            {
				               cout<<"ME\n"; 
						    }
		
							else if(rec[temid].ch2.compare("CE")==0&&rec[temid].per>=55)
				            {
				               cout<<"CE\n"; 
						    }
		
							else if(rec[temid].ch2.compare("EE")==0&&rec[temid].per>=50)
				            {
				               cout<<"EE\n"; 
						    }
		
							else if(rec[temid].ch3.compare("ME")==0&&rec[temid].per>=60)
				            {
				               cout<<"ME\n";
						    }
		
						    else if(rec[temid].ch3.compare("CE")==0&&rec[temid].per>=55)
				            {
				               cout<<"CE\n";
						    }
		
							else if(rec[temid].ch3.compare("EE")==0&&rec[temid].per>=50)
				            {
				               cout<<"EE\n";
						    }
					
				      }
					else
				      {
				        cout<<"\tFailed\n";
					   }
				}	    
				else 
			    {
			        cout<<"Roll No Not Found\n";	
			    }
			    	
		
				cout<<"\n\n1-Main\n2-Exit\nEnter Choice:";
		        cin>>ch;
				if(ch==1)
				goto start;
				if(ch==2)
				goto exit;
				break;    
			}
	
		case 6:
				goto exit;
				break;
	
		default:
				goto start;	
	}
	exit:
	closedisplay();
	
	return 0;
}

//Returns Department By Checking Choice & Percentage

void tryagain()
{
    for(int i=30;i>=0;i--)
    {
        cout<<"Try Again After:"<<i;
        Sleep(1000);
        system("cls");
    }
}

int checkchoice(string c)
{
	int ch;
    if(c.compare("CE")==0||c.compare("ME")==0||c.compare("EE")==0)
    ch=1;
    else
    ch=0;
    return ch;
}

//Displays Start Menu

void display()
{
	system("cls");
	cout<<"Please Wait";
	Sleep(1000);
    for(int i=1;i<6;i++)
    {
        cout<<".";
        Sleep(500);
    }
    system("cls");
    system("cls");
    cout<<"\t\t\t\t****************************************************\n\t";
    cout<<"\t\t\t*                    Entry Test                    *\n\t";
    cout<<"\t\t\t****************************************************\n\t";
    cout<<"\n\n1-Register Here";
    cout<<"\n\n2-Registerd";
	cout<<"\n\n3-Login";
	cout<<"\n\n4-Result All";   
	cout<<"\n\n5-Result Roll No";
    cout<<"\n\n6-Exit";
	cout<<"\n\nEnter Choice:";
}

//Displays Closing

void closedisplay()
{
	system("cls");
    cout<<"Closing";
    Sleep(1000);
    for(int i=1;i<6;i++)
    {
        cout<<".";
        Sleep(600);
    }
    system("cls");
                }
//find Unit And Tenth Digit
//and Returns It For Using To Search Recored
//for Eg 11601 Tenth Digit=0,Unit=1

int findrollno(int temprollno)
{
    int u,t,final;
    u=temprollno%10;
    t=(temprollno%100)/10;
    if(t==0)
    {
        final=u;
        return final;
    }	
	else if(t>0)
    {
        final=(t*10)+u;
	    return final;	
    }
}

void load()            
{         
    cout<<"Loading";
    for(int i=5;i>=0;i--)
    {
        cout<<".";
        Sleep(300);
    }
}

//Introduction About Program

void intro()
{
	Sleep(1000);	
	cout<<"************************************";
	Sleep(1000);
	cout<<"\n\tProject Co-ordinator       *\n";
	cout<<"\t--------------------       *\n";
	Sleep(100);
	cout<<"\t ";
	Sleep(100);
	cout<<"M";
	Sleep(100);
	cout<<"i";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"Q";
	Sleep(100);
	cout<<"u";
	Sleep(100);
	cout<<"r";
	Sleep(100);
	cout<<"r";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"t";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"U";
	Sleep(100);
	cout<<"l";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"A";
	Sleep(100);
	cout<<"i";
	Sleep(100);
	cout<<"n";
	cout<<"\t   *\n";
	cout<<"\t\t\t\t   *";
	Sleep(1000);
	cout<<"\n************************************";
	Sleep(1000);
	
	//group members
	
	cout<<"\n\tGroup Members\t\t   *";
	cout<<"\n\t-------------\t\t   *";
	cout<<"\n";
	Sleep(100);
	cout<<"1";
	Sleep(100);
	cout<<"-";
	Sleep(100);
	cout<<"M";
	Sleep(100);
	cout<<"u";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"d";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"H";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"n";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"M";
	Sleep(100);
	cout<<"u";
	Sleep(100);
	cout<<"g";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"l";
	cout<<"\t   *";
	Sleep(100);
	cout<<"\n";
	Sleep(100);
	cout<<"2";
	Sleep(100);
	cout<<"-";
	Sleep(100);
	cout<<"H";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"A";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"d";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"K";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"n";
	cout<<"\t\t   *";
	cout<<"\n";
	Sleep(100);
	cout<<"3";
	Sleep(100);
	cout<<"-";
	Sleep(100);
	cout<<"H";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"z";
	Sleep(100);
	cout<<"i";
	Sleep(100);
	cout<<"q";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"A";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"d";
	cout<<"\t\t\t   *";
	Sleep(100);
	cout<<"\n";
	Sleep(100);
	cout<<"4";
	Sleep(100);
	cout<<"-";
	Sleep(100);
	cout<<"U";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"e";
	Sleep(100);
	cout<<"r";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"B";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"i";
	Sleep(100);
	cout<<"t";
	cout<<"\t\t\t   *";
	cout<<"\n";
	Sleep(100);
	cout<<"5";
	Sleep(100);
	cout<<"-";
	Sleep(100);
	cout<<"M";
	Sleep(100);
	cout<<"u";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"a";
	Sleep(100);
	cout<<"d";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"M";
	Sleep(100);
	cout<<"e";
	Sleep(100);
	cout<<"h";
	Sleep(100);
	cout<<"m";
	Sleep(100);
	cout<<"o";
	Sleep(100);
	cout<<"o";
	Sleep(100);
	cout<<"d";
	cout<<"\t\t   *";
	Sleep(100);
	
	//project name
	
	cout<<"\n\t\t\t\t   *";
	Sleep(1000);
	cout<<"\n************************************";
	Sleep(1000);
	system("cls");
	Sleep(2000);
	cout<<"********************************************";
	Sleep(1000);
	cout<<"\n\t      Project:\t\t\t   *\n";
	cout<<"\t      --------\t\t\t   *\n";
	Sleep(100);
	cout<<"\tH";
	Sleep(100);
	cout<<"O";
	Sleep(100);
	cout<<"O";
	Sleep(100);
	cout<<"L";
	Sleep(100);
	cout<<"I";
	Sleep(100);
	cout<<"G";
	Sleep(100);
	cout<<"A";
	Sleep(100);
	cout<<"N";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<" ";
	cout<<"E";
	Sleep(100);
	cout<<"n";
	Sleep(100);
	cout<<"t";
	Sleep(100);
	cout<<"r";
	Sleep(100);
	cout<<"y";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"T";
	Sleep(100);
	cout<<"e";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"t";
	Sleep(100);
	cout<<" ";
	Sleep(100);
	cout<<"S";
	Sleep(100);
	cout<<"y";
	Sleep(100);
	cout<<"s";
	Sleep(100);
	cout<<"t";
	Sleep(100);
	cout<<"e";
	Sleep(100);
	cout<<"m";
	cout<<"\t   *";
	cout<<"\n\t\t\t\t\t   *";
	Sleep(1000);
	cout<<"\n********************************************\n";
	Sleep(1000);
	system("cls");
}
