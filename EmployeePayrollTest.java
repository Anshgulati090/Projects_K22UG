import com.bridgelabz.EmployeePayrollData;
import com.bridgelabz.EmployeePayrollService;
import com.bridgelabz.FileUtils;
import com.bridgelabz.IO_Service;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class EmployeePayrollTest {
    private static String HOME = System.getProperty("user.home");
    private static String PLAY_WITH_NIO = "TempPlayGround";

    @Test
    public void GivenPathWhenCheckedThenConfirm() throws IOException {
        // Check file existence
        Path homePath = Paths.get(HOME);
        Assert.assertTrue(Files.exists(homePath));

        // Delete file and check file non-existence
        Path playPath = Paths.get(HOME + "/" + PLAY_WITH_NIO);
        if (Files.exists(playPath))
            FileUtils.deleteFiles(playPath.toFile());
        Assert.assertTrue(Files.notExists(playPath));

        // Create Directory
        Files.createDirectories(playPath);
        Assert.assertTrue(Files.exists(playPath));

        // Create files using parallel stream
        IntStream.range(1, 10).parallel().forEach(cntr -> {
            Path tempFile = Paths.get(playPath + "/temp" + cntr);
            Assert.assertTrue(Files.notExists(tempFile));
            try {
                Files.createFile(tempFile);
            } catch (IOException e) {
                System.out.println("Catch");
            }
            Assert.assertTrue(Files.exists(tempFile));
        });

        // List files, directories, and files with extension
        Files.list(playPath).filter(Files::isRegularFile).forEach(System.out::println);
        Files.newDirectoryStream(playPath).forEach(System.out::println);
        Files.newDirectoryStream(playPath, path -> path.toFile().isFile() && path.toString().startsWith("temp"))
                .forEach(System.out::println);
    }

    @Test
    public void GivenThreeEmployeeWhenWrittenToFileAndReadShouldReturnCount() throws IOException {
        List<EmployeePayrollData> employeePayrollData = new ArrayList<>();
        EmployeePayrollData emp1 = new EmployeePayrollData(1, "Prajwal", 50000);
        EmployeePayrollData emp2 = new EmployeePayrollData(2, "Prajkta", 70000);
        EmployeePayrollData emp3 = new EmployeePayrollData(3, "Sarika", 60000);
        EmployeePayrollData emp4 = new EmployeePayrollData(4, "Dadasaheb", 80000);
        EmployeePayrollData emp5 = new EmployeePayrollData(5, "Ram", 50000000);
        employeePayrollData.add(emp1);
        employeePayrollData.add(emp2);
        employeePayrollData.add(emp3);
        employeePayrollData.add(emp4);
        employeePayrollData.add(emp5);
        EmployeePayrollService employeePayrollService = new EmployeePayrollService(employeePayrollData);

        // Use try-with-resources to ensure resources are closed properly
        try {
            employeePayrollService.writeData(IO_Service.FILE_IO);
            employeePayrollService.readData(IO_Service.FILE_IO);
            long count = employeePayrollService.CountEntries(IO_Service.FILE_IO);
            System.out.println("Total Count is: " + count);
            Assert.assertEquals(5, count);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
