import java.io.*;
import java.util.*;

public class ConvertBug {
	//ArrayList<ArrayList<Integer>> dag;
	HashMap<Integer, Integer> state = new HashMap<Integer, Integer>();
	int n_question;
	int m = 1;
	HashMap<Integer, ArrayList<Integer>> map_parents_id = new HashMap<Integer, ArrayList<Integer>>(); // map from s_id -> parents_id
	String dagFile;
	String stateFile;
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

	public String generateVal () {
		String res = "";
		res += "# the dag file is from " + dagFile + "\n";
		res += "# the state file is from " + stateFile + "\n";
		res += "var\n";
		res += "	";
		for (int j = 0; j < m; j ++) {
			for (int i = 0; i < n_question; i++) {
				res += "m" + j + "n" + i + "[N], ";
			}
			res += "\n	";
		}
		
		// System.out.println();
		// print the alpha matrix
		for (int i = 0; i < n_question; i++) {
			res += "n" + i + ".alpha" + "[";
			ArrayList<Integer> list = map_parents_id.get(i);
			for (Integer parents_id: list) {
				res += state.get(parents_id) + ",";
			}
			res += state.get(i) + "], ";
			
		}
		// print the p matrix
		for (int i = 0; i < n_question; i++) {
			res += "n" + i + ".prob" + "[";
			ArrayList<Integer> list = map_parents_id.get(i);
			for (Integer parents_id: list) {
				res += state.get(parents_id) + ",";
			}
			if (i != n_question - 1) {
				res += state.get(i) + "], ";
			} else {
				res += state.get(i) + "]\n";
			}
			
		}
		return res;
	}

	public String generateModel () {
		String res = "model {\n\n";
		// print the prob
		for (int i = 0; i < n_question; i++) {
			ArrayList<Integer> parents_id = map_parents_id.get(i);
			if (parents_id.size() == 0) {
				res += "	n" + i + ".prob[] ~ ddirich(" + "n" + i + ".alpha[])\n";
			} else {
				ArrayList<String> combine = generateProbModel("", 0, parents_id);
				for (String s : combine) {
					res += "	n" + i + ".prob" + s + " ~ ddirich(n" + i + ".alpha" + s + ")\n";
				}
			}
			
		}
		// print the directed graphic model
		res += "\n";
		res += "	for (i in 1:N) {\n";
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n_question; i++) {
				res += "		" + "m" + j + "n" + i + "[i]" + " ~ dcat(n" + i + ".prob[";
				ArrayList<Integer> parents_id = map_parents_id.get(i);
				for (Integer p_id : parents_id) {
					res += "m" + j + "n" + p_id + "[i],";
				}
				res += "])\n";
			}
		}
		
		res += "	}\n";
		res += "}";
		return res;
	}

	// everything should start from 1
	public ArrayList<String> generateProbModel (String prev, int i, ArrayList<Integer> parents_id) {
		int N = state.get(parents_id.get(i));
		if (i == 0) {
			ArrayList<String> res = new ArrayList<String>();
			for (int j = 1; j <= N; j++) {
				String revised_prev = "[" + j + ",";
				if (parents_id.size() == 1) {
					// we done
					revised_prev += "]";
					res.add(revised_prev);
				} else {
					res.addAll((Collection<String>)generateProbModel(revised_prev, 1, parents_id));
				}
			}
			return res;
		} else if (i == parents_id.size() - 1) {
			ArrayList<String> res = new ArrayList<String>();
			for (int j = 1; j <= N; j++) {
				String revised_prev = prev + j + ",]";
				res.add(revised_prev);
			}
			return res;
		} else {
			ArrayList<String> res = new ArrayList<String>();
			for (int j = 1; j <= N; j++) {
				String revised_prev = prev + j + ",";
				res.addAll((Collection<String>)generateProbModel(revised_prev, i + 1, parents_id));
			}
			return res;
		}
	}

	public void testPrintDag () {
		System.out.println("number of node is " + n_question);
		for (int i = 0; i < n_question; i++) {
			System.out.print("Id is " + i + ": ");
			ArrayList<Integer> tmp = map_parents_id.get(i);
			for (Integer id : tmp) {
				System.out.print(id + "; ");
			}
			System.out.println();
		}
	}
	public void testPrintState () {
		for (int i = 0; i < n_question; i++) {
			System.out.println("Id is " + i + ": " + state.get(i));
		}
	}

	public void printSummary () {
		System.out.println("num of the states are " + n_question);
		System.out.println("Dim of the states are " + state.size());
		System.out.println("Dim of the dag are " + map_parents_id.size());

	}
	public static void main(String[] args) {

		String dag = args[0];
		String state = args[1];
		ConvertBug convert = new ConvertBug();
		convert.m = Integer.parseInt(args[2]);

		convert.readInDag(dag);
		convert.readInState(state);
		// System.out.println("finish read");
		// convert.printSummary();
		// convert.testPrintDag();
		// convert.testPrintState();
		String val = convert.generateVal();
		String model = convert.generateModel();
		try {
			File file = new File("./bugfile");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			bw.write(val);
			bw.write(model);
			bw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		// System.out.println(convert.generateVal());
		// System.out.println(convert.generateModel());
		
		
	}

}