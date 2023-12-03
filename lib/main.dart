import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
// import 'package:collection/collection.dart';
// import 'package:geocode/geocode.dart';
import 'package:latlong2/latlong.dart';
// import 'package:tuple/tuple.dart';
// import 'package:positioned_tap_detector_2/positioned_tap_detector_2.dart';
// import 'package:transparent_image/transparent_image.dart';
// import 'package:async/async.dart';
// import 'package:flutter_image/flutter_image.dart';
// import 'package:vector_math/vector_math.dart';
// import 'package:proj4dart/proj4dart.dart';
// import 'package:meta/meta.dart';
// import 'package:collection/collection.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Stack(
        children: [
          FlutterMap(
            options: MapOptions(
              center: LatLng(49.5, -0.09), // center of the map
              zoom: 1.0
            ),
            children: [
              TileLayer(
                    urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                    userAgentPackageName: 'com.example.app',
                ),
                MarkerLayer(
                  markers: [
                    Marker(
                      width: 100.0,
                      height: 100.0,
                      point: LatLng(49.5, -0.09), 
                      child: Icon(
                          Icons.location_on,
                          color: Colors.red,
                        ),
                    )
                  ],
                )
            ],
          )
        ],
      ),
    );
  }
}
