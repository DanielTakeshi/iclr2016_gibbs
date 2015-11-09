import java.io.*;
import java.util.*;

public class ConvertR {
	HashMap<Integer, Integer> state = new HashMap<Integer, Integer>();
	int n_question;
	int n_student;
	int m;
	HashMap<Integer, ArrayList<Integer>> map_parents_id = new HashMap<Integer, ArrayList<Integer>>(); // map from s_id -> parents_id
	ArrayList<ArrayList<Integer>> sdata = new ArrayList<ArrayList<Integer>>();
	String dagFile;
	String stateFile;
	String sdataFile;

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

	public void readSdata (String fileName) {
		try {
			FileInputStream fstream = new FileInputStream(fileName);
			stateFile = fileName;
			BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

			String line;
			int i = 0;
			while ((line = br.readLine()) != null) {
	   		// process the line.
				String[] line_split = line.split("\\s+");
				ArrayList<Integer> tmp = new ArrayList<Integer>();
				for (int dst = 0; dst < line_split.length; dst++) {
					tmp.add((int)Float.parseFloat(line_split[dst]));
				}
				// System.out.println();
				n_student = line_split.length;
				sdata.add(tmp);
			}
		} catch (FileNotFoundException e) {
			System.err.println("Caught FileNotFoundException: " + e.getMessage());
		} catch (IOException e) {
			System.err.println("Caught IOException: " + e.getMessage());
		}
	}

	public String generateAlpha () {
		String res = "# generate alpha data\n";
		for (int i = 0; i < n_question; i++) {
			ArrayList<Integer> tmp = map_parents_id.get(i);
			if (tmp.size() == 0) {
				res += "n" + i + ".alpha <- c(";
				for (int j = 0; j < state.get(i); j++) {
					if (j != state.get(i) - 1) {
						res += "1, ";
					} else {
						res += "1)\n";
					}
					
				}
			} else {
				res += "n" + i + ".alpha <- structure(c(";
				int tot_num = state.get(i);
				for (Integer parents_id : tmp) {
					tot_num *= state.get(parents_id);
				}
				for (int j = 0; j < tot_num; j++) {
					if (j != tot_num - 1) {
						res += "1, ";
					} else {
						res += "1), .Dim = as.integer(c(";
					}
				}
				for (Integer parents_id : tmp) {
					res += state.get(parents_id) + ",";
				}
				res += state.get(i) + ")))\n";
			}
		}
		res += "\n";
		return res;
	}

	public String generateSdata () {
		StringBuffer res = new StringBuffer("# start of the data\n");
		for (int j = 0; j < m; j++) {
			System.out.println("generating sdata:" + j + "/" + m);
			for (int i = 0; i < n_question; i++) {
				res.append("m" + j + "n" + i + "<-c(");
				ArrayList<Integer> list = sdata.get(i);
				for (int k = 0; k < n_student; k++) {
					int val = list.get(k);
					String val_s = "";
					if (val == 0) {
						val_s = "NA";
					} else {
						val_s = "" + val;
					}
					if (k != n_student - 1) {

						res.append(val_s + ",");
					} else {
						res.append(val_s + ")\n");
					}
				}
			}
		}
		res.append("\n");
		res.append("N <- " + n_student + "\n");
		return res.toString();
	}

	public String generateList () {
		String res = "# generate data list\n";
		res += "data_list <- list (";
		// print the alpha value
		for (int i = 0; i < n_question; i++) {
			res +="'n" + i + ".alpha' = " + "n" + i + ".alpha,\n";
		}
		// print the N value
		res += "'N' = " + n_student + ",\n";

		// print the nodes

		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n_question; i++) {
				if (j == m - 1 && i == n_question - 1) {
					res += "'m" + j + "n" + i +"' = " + "m" + j + "n" + i + ")\n";
				} else {
					res += "'m" + j + "n" + i +"' = " + "m" + j + "n" + i + ",\n";
				}
				
			}
		}
		return res;
	}

	public static void main(String[] args) {
		String dagFile = args[0];
		String stateFile = args[1];
		String sdataFile = args[2];
		ConvertR convertR = new ConvertR();
		convertR.m = Integer.parseInt(args[3]);

		convertR.readInDag(dagFile);
		convertR.readInState(stateFile);
		convertR.readSdata(sdataFile);
		if (args.length == 5) {
			convertR.n_student = Integer.parseInt(args[4]);
		}
		String alpha = convertR.generateAlpha();
		// System.out.println("finish alpha");
		String sdata = convertR.generateSdata();
		// System.out.println("finish the sdata");
		String list = convertR.generateList();
		// System.out.println("finish generate");
		try {
			File file = new File("./data.r");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(alpha);
			bw.write(sdata);
			//bw.write(list);
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		// System.out.println(alpha);
		// System.out.println(sdata);
		// System.out.println(list);
	}

}