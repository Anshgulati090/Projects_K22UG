package com.bridgelabz;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class EmployeePayrollService {


    List<EmployeePayrollData> employeePayrollList;

    public EmployeePayrollService(List<EmployeePayrollData> list) {
        this.employeePayrollList=list;
    }

    public void writeData(IO_Service ioType) throws IOException {
        PayrollService payrollService;
        if(IO_Service.FILE_IO.equals(ioType)){
            payrollService=new FileIOImpl();
        } else if (IO_Service.CONSOLE_IO.equals(ioType)) {
            payrollService=new ConsoleIOImpl();
        } else if (IO_Service.CLOUD_IO.equals(ioType)) {
            payrollService= new CloudIOImpl();
        }else {
            payrollService=new DatabaseIOImpl();
        }
        payrollService.writeData(employeePayrollList);
    }

    public void readData(IO_Service ioType) throws IOException {
        PayrollService payrollService;
        if(IO_Service.FILE_IO.equals(ioType)){
            payrollService=new FileIOImpl();
        } else if (IO_Service.CONSOLE_IO.equals(ioType)) {
            payrollService=new ConsoleIOImpl();
        } else if (IO_Service.CLOUD_IO.equals(ioType)) {
            payrollService= new CloudIOImpl();
        }else {
            payrollService=new DatabaseIOImpl();
        }
        payrollService.readData();
    }
    public Long CountEntries(IO_Service ioType) {
        PayrollService payrollService;
        if(IO_Service.FILE_IO.equals(ioType)){
            payrollService=new FileIOImpl();
        } else if (IO_Service.CONSOLE_IO.equals(ioType)) {
            payrollService=new ConsoleIOImpl();
        } else if (IO_Service.CLOUD_IO.equals(ioType)) {
            payrollService= new CloudIOImpl();
        }else {
            payrollService=new DatabaseIOImpl();
        }
        try {
            return payrollService.count();
        } catch (IOException e) {
            System.out.println("Catch block");
        }
        return null;
    }

    public void read(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter ID :- ");
        int id=sc.nextInt();
        System.out.println("Enter Name :- ");
        String name=sc.next();
        System.out.println("Enter salary :- ");
        double salary=sc.nextDouble();
        employeePayrollList.add(new EmployeePayrollData(id,name,salary));
    }

    public void write(){
        System.out.println(employeePayrollList);
    }

    public static void main(String[] args) {
         List<EmployeePayrollData> employeePayrollList= new ArrayList<>();
         EmployeePayrollService employeePayrollService = new EmployeePayrollService(employeePayrollList);
        employeePayrollService.read();
        employeePayrollService.write();
    }


}
