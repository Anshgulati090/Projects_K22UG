package com.bridgelabz;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FileIOImpl implements PayrollService {
    @Override
    public void writeData(List<EmployeePayrollData> list) throws IOException {
        String path = "C:\\Users\\prajw\\IdeaProjects\\EmployeePayroll\\src\\main\\java\\com\\bridgelabz\\data.txt";
        StringBuffer stringBuffer = new StringBuffer();
        list.stream().forEach(employee->{
            String empString = employee.toString().concat("\n");
            stringBuffer.append(empString);
        });
        Files.write(Path.of(path),stringBuffer.toString().getBytes());
    }

    @Override
    public void readData() throws IOException {
        String path = "C:\\Users\\prajw\\IdeaProjects\\EmployeePayroll\\src\\main\\java\\com\\bridgelabz\\data.txt";
        Files.lines(Path.of(path)).forEach(System.out::println);

    }

    @Override
    public long count() throws IOException {
        String path = "C:\\Users\\prajw\\IdeaProjects\\EmployeePayroll\\src\\main\\java\\com\\bridgelabz\\data.txt";
        return Files.lines(Path.of(path)).count();
    }
}
