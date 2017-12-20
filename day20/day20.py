import collections

Particle = collections.namedtuple('Particle', ['p', 'v', 'a'])


def manh(vec):
    return sum(map(abs, vec))


def particle_from_line(line):
    p, v, a = line.strip().split(', ')
    return Particle(to_vec(p), to_vec(v), to_vec(a))


def to_vec(s):
    return tuple(map(int, s[3:-1].split(',')))


def multiply(vec, scalar):
    return tuple(value * scalar for value in vec)


def sum_vectors(*vecs):
    return tuple(sum(x) for x in zip(*vecs))


def particles_from_file(file_name):
    with open(file_name) as fh:
        return [particle_from_line(line) for line in fh]


def position_after(particle, t):
    da = multiply(particle.a, t*t/2)
    dv = multiply(particle.v, t)
    dp = particle.p
    return sum_vectors(da, dv, dp)


def part1():
    particles = particles_from_file('input.txt')
    min_a = manh(min(particles, key=lambda p: manh(p.a)).a)
    candidates = [(idx, p) for idx, p in enumerate(particles)
                  if manh(p.a) == min_a]
    # this T=10000 is just an ugly magic number
    # we _really_ need solution which "just knows"
    # but simple sort based on (a, v, p) has it's false positives
    result = min(candidates, key=lambda c: manh(position_after(c[1], t=1000)))
    print("part 1 result is", result)


def simulate(particle):
    v = sum_vectors(particle.v, particle.a)
    p = sum_vectors(particle.p, v)
    return Particle(p, v, particle.a)


def destroy_collided(particles):
    positions = collections.defaultdict(list)
    for particle in particles:
        positions[particle.p].append(particle)
    return [p for p in particles if len(positions[p.p]) == 1]


def part2():
    particles = particles_from_file('input.txt')
    particles = destroy_collided(particles)
    for _ in range(1000):
        particles = [simulate(p) for p in particles]
        particles = destroy_collided(particles)
    print("part 2 result is", len(particles))


if __name__ == "__main__":
    # I'm really not happy about it, both solutions are just ugly brute-force
    part1()
    part2()
