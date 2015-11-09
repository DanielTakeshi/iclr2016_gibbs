import java.io.*;
import java.util.*;

public class GenerateJagsExe {
	HashMap<Integer, Integer> state = new HashMap<Integer, Integer>();
	int n_question;
	int m = 1;
	HashMap<Integer, ArrayList<Integer>> map_parents_id = new HashMap<Integer, ArrayList<Integer>>(); // map from s_id -> parents_id
	String dagFile;
	String stateFile;
	String bugFile;
	String dataFile;
	int n_update;

	public void readInDag (String fileName) {
		try {
			FileInputStream fstream = new FileInputStream(fileName);
			dagFile = fileName;
			BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

			String line;
			int i = 0;
			while ((line = br.readLine()) != null) {
	   		// process the line.
				String[] line_split = line.split("\\s+");
				ArrayList<Integer> tmp = new ArrayList<Integer>();
				for (int dst = 0; dst < line_split.length; dst++) {
					if (Float.parseFloat(line_split[dst]) == 1.0) {
	    				tmp.add(dst);
					}
				}
				// System.out.println();
				map_parents_id.put(i, tmp);
				i++;
			}
			n_question = i;
		} catch (FileNotFoundException e) {
			System.err.println("Caught FileNotFoundException: " + e.getMessage());
		} catch (IOException e) {
			System.err.println("Caught IOException: " + e.getMessage());
		}
	}

	public void readInState (String fileName) {
		try {
			FileInputStream fstream = new FileInputStream(fileName);
			stateFile = fileName;
			BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

			String line;
			int i = 0;
			while ((line = br.readLine()) != null) {
	   		// process the line.
				int size = Math.round(Float.parseFloat(line));
				state.put(i, size);
				i++;
			}
		} catch (FileNotFoundException e) {
			System.err.println("Caught FileNotFoundException: " + e.getMessage());
		} catch (IOException e) {
			System.err.println("Caught IOException: " + e.getMessage());
		}
		
	}

	public String generateExe () {
		StringBuffer res = new StringBuffer("# exe file for jags\n");
		res.append("# from " + dagFile + "; " + stateFile + "\n");
		res.append("model in \"" + bugFile + "\"\n");
		res.append("data in \"" + dataFile + "\"\n");

		res.append("compile, nchains(1)\n");
		res.append("initialize\n");
		// monitor all the nodes
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n_question; i++) {
				res.append("monitor m" + j + "n" + i + "\n");
			}
		}

		// monitor all probs
		for (int i = 0; i < n_question; i++) {
			res.append("monitor n" + i + ".prob\n");
		}
		res.append("update " + n_update + "\n");
		res.append("coda *\n");
		return res.toString();
	}

	public static void main(String[] args) {
		String dag = args[0];
		String state = args[1];
		GenerateJagsExe convert = new GenerateJagsExe();
		convert.m = Integer.parseInt(args[2]);
		convert.bugFile = args[3];
		convert.dataFile = args[4];
		convert.n_update = Integer.parseInt(args[5]);
		convert.readInDag(dag);
		convert.readInState(state);
		// System.out.println("finish read");
		// convert.printSummary();
		// convert.testPrintDag();
		// convert.testPrintState();
		String val = convert.generateExe();
		try {
			File file = new File("./runJagsExe");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(val);
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		// System.out.println(val);
		
	}
}