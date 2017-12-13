package main

import (
	"reflect"
	"testing"
)

func TestTravel(t *testing.T) {
	testTravel := TravelFromFile("test.txt")
	detections := GetDetections(&testTravel)
	expected := []int{0, 6}
	if !reflect.DeepEqual(detections, expected) {
		t.Errorf("Got: %d, want: %d.", detections, expected)
	}
	expected2 := 24
	result2 := Severity(&testTravel, detections)
	if result2 != expected2 {
		t.Errorf("Got: %d, want: %d.", result2, expected2)
	}
}

func TestDelay(t *testing.T) {
	testTravel := TravelFromFile("test.txt")
	delay := GetNeededDelay(&testTravel)
	expected := 10
	if delay != expected {
		t.Errorf("Got: %d, want: %d.", delay, expected)
	}
}
