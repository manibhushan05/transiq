package in.aaho.android.driver.common;

/**
 * Created by shobhit on 3/11/16.
 */

/*******************************************************************************
 * Copyright (c) 2013 Chris Banes.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/


import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;


class IoUtils {

    private static final String LOG_TAG = "[IoUtils]";

    public static void closeStream(InputStream is) {
        if (is != null) {
            try {
                is.close();
            } catch (IOException e) {
                Log.i(LOG_TAG, "Failed to close InputStream", e);
            }
        }
    }

    public static void closeStream(OutputStream os) {
        if (os != null) {
            try {
                os.close();
            } catch (IOException e) {
                Log.i(LOG_TAG, "Failed to close OutputStream", e);
            }
        }
    }

    public static long copy(File in, OutputStream out) throws IOException {
        return copy(new FileInputStream(in), out);
    }

    public static long copy(InputStream in, File out) throws IOException {
        return copy(in, new FileOutputStream(out));
    }

    /**
     * Pipe an InputStream to the given OutputStream <p /> Taken from Apache Commons IOUtils.
     */
    public static long copy(InputStream input, OutputStream output) throws IOException {
        try {
            byte[] buffer = new byte[1024 * 4];
            long count = 0;
            int n;
            while (-1 != (n = input.read(buffer))) {
                output.write(buffer, 0, n);
                count += n;
            }
            output.flush();
            return count;
        } finally {
            IoUtils.closeStream(input);
            IoUtils.closeStream(output);
        }
    }

}