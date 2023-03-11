// Java code for the above DFA
import java.util.*;

class GFG{

// Function for the state A
static void checkstatea(String n)
{
if (n.length() % 2 != 0 ||
	n.length() < 4)
	System.out.print("string not accepted");
else
{
	int i = 0;
	
	// State transition to B
	// if the character is 0
	if (n.charAt(i) == '0')
	stateb(n.substring(1));
	else
	System.out.print("string not accepted");
}
}

// Function for the state B
static void stateb(String n)
{
int i = 0;

if (n.charAt(i) == '0')
	System.out.print("string not accepted");

// State transition to C
// if the character is 1
else
	statec(n.substring(1));
}

// Function for the state C
static void statec(String n)
{
int i = 0;

// State transition to D
// if the character is 1
if (n.charAt(i) == '1')
	stated(n.substring(1));

// State transition to B
// if the character is 0
else
	stateb(n.substring(1));
}

// Function for the state D
static void stated(String n)
{
int i = 0;

if (n.length() == 1)
{
	if (n.charAt(i) == '1')
	System.out.print("string accepted");
	else
	System.out.print("string not accepted");
}
else
{
	
	// State transition to E
	// if the character is 1
	if (n.charAt(i) == '1')
	statee(n.substring(1));
	else
	System.out.print("string not accepted");
}
}

// Function for the state E	
static void statee(String n)
{
int i = 0;

if (n.length() == 1)
{
	if (n.charAt(i) == '0')
	System.out.print("string not accepted");
	else
	System.out.print("string accepted");
}
else
{
	if (n.charAt(i) == '0')
	System.out.print("string not accepted");
	
	stated(n.substring(1));
}
}
	
// Driver code
public static void main(String []args)
{

// Take string input
String n ="011111";

// Call stateA to check the input
checkstatea(n);
}
}

// This code is contributed by pratham76
