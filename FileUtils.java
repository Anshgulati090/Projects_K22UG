package com.bridgelabz;

import java.io.File;
import java.util.Objects;

public class FileUtils {
    public static boolean deleteFiles(File contentsToDelete) {
        if (contentsToDelete == null || !contentsToDelete.exists()) {
            return false;
        }

        File[] allContents = contentsToDelete.listFiles();

        if (allContents != null) {
            for (File file : allContents) {
                deleteFiles(file);
            }
        }
        
        return contentsToDelete.delete();
    }
}
