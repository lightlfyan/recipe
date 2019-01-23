
use_bpm 70
use_octave 0.2

define :bass_track do
  live_loop :bass do
    use_synth :fm
    play 52
    sleep 1
    play 60
    sleep 1
    play 55
    sleep 1
    play 54
    sleep 1
  end
end

define :drum_track do
  live_loop :drums do
    sample :drum_bass_hard
    sleep 0.5
    sample :drum_bass_hard
    sleep 0.5
    sample :drum_snare_hard
    sleep 0.5
    sample :drum_bass_soft
    sleep 0.25
    sample :drum_snare_soft
    sleep 0.25
  end
end


define :play_phrase do
  use_synth :fm
  with_fx :reverb, phase: 0.125 do
    notes = [:e3, :e4, :b4, :g4,
             :c4, :e4, :c5, :g4,
             :g3, :d4, :b4, :g4,
             :gb4, :g4, :a4, :d4]
    i = 0
    16.times do
      note = notes[i]
      play note, sustain: 0.3
      sleep 0.5
      i = i+1
    end
  end
end

in_thread do
  8.times do
    play_phrase
  end
end


in_thread do
  sleep 8
  drum_track
end

in_thread do
  sleep 8
  bass_track
end


