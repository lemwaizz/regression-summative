import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MonkeyPoxApp());
}

class MonkeyPoxApp extends StatelessWidget {
  const MonkeyPoxApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Monkey Pox Predictor',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const PredictionScreen(),
    );
  }
}

class PredictionScreen extends StatefulWidget {
  const PredictionScreen({super.key});

  @override
  _PredictionScreenState createState() => _PredictionScreenState();
}

class _PredictionScreenState extends State<PredictionScreen> {
  final TextEditingController _controller = TextEditingController();
  final List<String> symptoms = [
    'Rectal_Pain',
    'Sore_Throat',
    'Penile_Oedema',
    'Oral_Lesions',
    'Solitary_Leision',
    'Swollen_Tonsils',
    'HIV_Infection',
    'STI',
    'Systemic_Illness_Fever',
    'Systemic_Illness_Muscle_Aches_and_Pain',
    'Systemic_Illness_Swollen_Lymph_Nodes',
    'Target'
  ];
  final Map<String, int> inputs = {};
  String output = "";

  @override
  void initState() {
    super.initState();
    for (var symptom in symptoms) {
      inputs[symptom] = 0;
    }
  }

  Future<void> predict() async {
    const String apiUrl = "https://regression-summative.onrender.com/predict";
    try {
      final response = await http.post(
        Uri.parse(apiUrl),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(inputs),
      );

      if (response.statusCode == 200) {
        final decodedResponse = jsonDecode(response.body);
        bool diagnosis = decodedResponse['Monkey Pox Diagnosis']
            [0]; // Extracting the first value
        setState(() {
          output =
              "Monkey Pox Diagnosis: ${diagnosis ? 'Positive' : 'Negative'}";
        });
      } else {
        setState(() {
          output = "Error: ${response.body}";
        });
      }
    } catch (e) {
      setState(() {
        output = "Failed to connect to API";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Monkey Pox Predictor')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Expanded(
              child: ListView(
                children: symptoms.map((symptom) {
                  return TextField(
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      labelText: symptom.replaceAll('_', ' '),
                      border: const OutlineInputBorder(),
                    ),
                    onChanged: (value) {
                      setState(() {
                        inputs[symptom] = int.tryParse(value) ?? 0;
                      });
                    },
                  );
                }).toList(),
              ),
            ),
            ElevatedButton(
              onPressed: predict,
              child: const Text('Predict'),
            ),
            const SizedBox(height: 20),
            Text(output,
                style:
                    const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
    );
  }
}
