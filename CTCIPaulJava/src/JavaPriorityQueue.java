import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.*;
/*
 * Create the Student and Priorities classes here.
 */ 
class Student{
    String name;
    double cgpa;
    int id;
    
    Student(String n, double c, int i){
        name = n;
        cgpa = c;
        id = i;
    }
    String getName(){ return name;}
    double getCGPA(){ return cgpa;}
    int getID(){ return id;}
    
    void printStudent(){
        System.out.println(getName() + " " + getCGPA() + " " + getID());
    }
    
}

class Priorities{
    
    //Comparator anonymous class implementation
	public static Comparator<Student> idComparator = new Comparator<Student>(){
		
		@Override
		public int compare(Student a, Student b) {
            if (a.getCGPA() > b.getCGPA()){ // compare first by GPA
                return -1;
            }
            else if (a.getCGPA() < b.getCGPA()){
                return 1;
            }
            else if (a.getCGPA() == b.getCGPA()){ //if gpa is same, go by name
                if (a.getName().compareTo(b.getName()) > 0) {//a is greater{
                    return 1;
                }
                else if (a.getName().compareTo(b.getName()) < 0){
                    return -1;
                }
                else{ //if the gpa is same and name is same, we go by id
                    return (a.getID() > b.getID()) ? -1 : 1;
                }
            }
            else { //shouldnt even go here
                System.out.println("why would it go here");
                a.printStudent();
                b.printStudent();
                return 1;
            }
        }
	};
    public List<Student> getStudents(List<String> events){
        //init pqueue here
        List<Student> unservedStudents2 = new ArrayList<Student>();
        Queue<Student> unservedStudents = new PriorityQueue<Student>(events.size(), idComparator);
        for (String event: events){
            if (event.startsWith("ENTER")){
                String[] splitted = event.split("\\s+");
                String newName = splitted[1];
                double newCGPA = Double.parseDouble(splitted[2]);
                int newID = Integer.parseInt(splitted[3]);
                                                
                Student newStudent = new Student(newName, newCGPA, newID);
                unservedStudents.add(newStudent);
            }
            else if (event.equals("SERVED")){
                //get the highest GPA student if his name is unique
                unservedStudents.poll();
            }  
        }
        //insert elements from pqueue into arraylist
        //this has to be done for some reason or ordering gets fucked up
        while (!unservedStudents.isEmpty()){
            unservedStudents2.add(unservedStudents.poll());
        }
        
        return unservedStudents2;
    }
}

public class Solution {
    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();
    
    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());    
        List<String> events = new ArrayList<>();
        
        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }
        
        List<Student> students = priorities.getStudents(events);
        
        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st: students) {
                System.out.println(st.getName());
            }
        }
    }
}