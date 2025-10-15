import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Password Generator',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const MyHomePage(title: 'Password Generator Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;
  const MyHomePage({super.key, required this.title});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int passwordLength = 12;
  bool includeUppercase = false;
  bool includeNumbers = false;
  bool includeSpecialChars = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title)),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            const Text(
              'Generador de contraseñas',
              style: TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 16),

            // Selector de longitud
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [const Text('Longitud'), Text('$passwordLength')],
            ),
            Slider(
              value: passwordLength.toDouble(),
              min: 4,
              max: 64,
              divisions: 60,
              label: passwordLength.toString(),
              onChanged: (v) => setState(() => passwordLength = v.round()),
            ),

            // Opciones
            SwitchListTile(
              title: const Text('Incluir mayúsculas'),
              value: includeUppercase,
              onChanged: (v) => setState(() => includeUppercase = v),
            ),
            SwitchListTile(
              title: const Text('Incluir números'),
              value: includeNumbers,
              onChanged: (v) => setState(() => includeNumbers = v),
            ),
            SwitchListTile(
              title: const Text('Incluir símbolos'),
              value: includeSpecialChars,
              onChanged: (v) => setState(() => includeSpecialChars = v),
            ),

            const SizedBox(height: 12),
            ElevatedButton(
              onPressed: () {
                final pw = generarContrasena(
                  passwordLength,
                  includeUppercase,
                  includeNumbers,
                  includeSpecialChars,
                );
                showDialog(
                  context: context,
                  builder:
                      (_) => AlertDialog(
                        title: const Text('Contraseña generada'),
                        content: SelectableText(pw),
                        actions: [
                          TextButton(
                            onPressed: () => Navigator.of(context).pop(),
                            child: const Text('Cerrar'),
                          ),
                        ],
                      ),
                );
              },
              child: const Text('Generar contraseña'),
            ),
          ],
        ),
      ),
    );
  }
}

String generarContrasena(
  int passwordLength,
  bool includeUppercase,
  bool includeNumbers,
  bool includeSpecialChars,
) {
  // Conjuntos de caracteres
  const lower = 'abcdefghijklmnopqrstuvwxyz';
  const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const numbers = '0123456789';
  const special = r'!@#\$%&*()-_=+[]{};:,.<>?/~';

  // Construir la piscina de caracteres
  String pool = lower;
  if (includeUppercase) pool += upper;
  if (includeNumbers) pool += numbers;
  if (includeSpecialChars) pool += special;

  // Asegurar al menos un carácter de cada tipo seleccionado
  final rng = Random.secure();
  final List<String> chars = [];

  int requiredTypes = 1; // lower siempre está presente
  if (includeUppercase) requiredTypes++;
  if (includeNumbers) requiredTypes++;
  if (includeSpecialChars) requiredTypes++;

  // Si la longitud solicitada es menor que el número de tipos requeridos, ajustar
  if (passwordLength < requiredTypes) passwordLength = requiredTypes;

  if (includeUppercase) chars.add(upper[rng.nextInt(upper.length)]);
  if (includeNumbers) chars.add(numbers[rng.nextInt(numbers.length)]);
  if (includeSpecialChars) chars.add(special[rng.nextInt(special.length)]);
  // Siempre añadir al menos una minúscula
  chars.add(lower[rng.nextInt(lower.length)]);

  // Rellenar el resto desde la piscina completa
  while (chars.length < passwordLength) {
    chars.add(pool[rng.nextInt(pool.length)]);
  }

  // Mezclar los caracteres para no dejar los asegurados al inicio
  chars.shuffle(rng);

  return chars.join();
}
