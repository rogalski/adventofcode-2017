package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const DOWN int = 1
const UP int = -1

const PACKET_ROUTE int = 0

type firewall_travel struct {
	layers     map[int]int
	positions  map[int]int
	directions map[int]int
	layercount int
}

func TravelFromFile(filename string) firewall_travel {
	travel := firewall_travel{make(map[int]int), make(map[int]int), make(map[int]int), 0}

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		v := strings.Split(line, ": ")
		layer, err := strconv.Atoi(v[0])
		if err != nil {
			log.Fatal(err)
			continue
		}
		depth, err := strconv.Atoi(v[1])
		if err != nil {
			log.Fatal(err)
			continue
		}
		travel.layers[layer] = depth
		travel.positions[layer] = -1
		travel.directions[layer] = DOWN
		if layer > travel.layercount {
			travel.layercount = layer
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return travel
}

func MoveScanners(travel *firewall_travel) {
	for layer := range travel.positions {
		travel.positions[layer] = travel.positions[layer] + travel.directions[layer]
		if travel.positions[layer] == 0 && travel.directions[layer] == UP {
			travel.directions[layer] = DOWN
		} else if travel.positions[layer] == (travel.layers[layer]-1) && travel.directions[layer] == DOWN {
			travel.directions[layer] = UP
		}
	}
}

func GetDetections(travel *firewall_travel) []int {
	var detections []int
	packetLayer := -1
	for packetLayer < travel.layercount {
		MoveScanners(travel)
		packetLayer++
		if pos, ok := travel.positions[packetLayer]; ok {
			if pos == PACKET_ROUTE {
				detections = append(detections, packetLayer)
			}
		}
	}
	return detections
}

func Severity(travel *firewall_travel, detections []int) int {
	sum := 0
	for _, num := range detections {
		sum += num * travel.layers[num]
	}
	return sum
}

func GetNeededDelay(travel *firewall_travel) int {
	// given _t_ we can compute position of each layer in const time
	// layer is periodic sequence of 0, 1, 2, .. N-1, n-2 .. 0 (period = 2*(N-1))
	delay := -1
	delay_ok := false
	for {
		delay += 1
		delay_ok = true
		for layer, depth := range travel.layers {
			if Lane(delay+layer, depth) == PACKET_ROUTE {
				// this delay would cause a collision
				delay_ok = false
				break
			}
		}
		if delay_ok {
			return delay
		}
	}
	return -1
}

func Lane(t int, N int) int {
	M := 2 * (N - 1)
	t = t % M
	if t > M/2 {
		return M - t
	}
	return t
}

func main() {
	testTravel := TravelFromFile("input.txt")
	detections := GetDetections(&testTravel)
	fmt.Println("Solution to part 1 is:", Severity(&testTravel, detections))
	fmt.Println("Solution to part 2 is:", GetNeededDelay(&testTravel))
}
