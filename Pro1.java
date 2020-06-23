package factoryysc;

import java.util.Scanner;
import java.util.*;

public class Pro1 {
	public static void main(String[] args) {
		ArrayList<Integer> alist = new ArrayList<Integer>();
				
		Scanner sc = new Scanner(System.in);
		String testCase = sc.nextLine();
		int tc = Integer.parseInt(testCase);
		for(int d =0; d < tc; d++) {
			String numCount = sc.nextLine();
			int nc = Integer.parseInt(numCount);
			
			String s1 = sc.nextLine();
			Judge ju = new Judge(s1);
			int tem = ju.getaws();
			alist.add(tem);
			
			for(int j = 0; j < tc; j++) {
				System.out.printf("#%d %d\n",j+1,alist.get(j));
			}
		}		
	}
}

class Judge{
	ArrayList<Integer> al = new ArrayList<Integer>();
	String s;
	
	Judge(String s){
		this.s = s;
	}
	
	public  int getaws(){
		
		int aws;
		String[] ss;
		ss = s.split(" ");
		int i;
		for(i = 0; i < ss.length; i++) {
			int tem = Integer.parseInt(ss[i]);
			al.add(tem);
		}
		
		Collections c = null;
		c.sort(al);
		
		aws = (al.get(al.size()-1) - al.get(0));
		
		return aws;
	}
	
	
}
