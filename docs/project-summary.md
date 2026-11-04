# Oden — Project Summary

[← Back to README](../README.md)

## 1. Overview

Oden is a local-first personal AI system intended to capture, understand, remember, and eventually act on information expressed through speech.

The project originated as a personal Speech-to-Text tool for recording thoughts and ideas without interrupting the user's workflow.

The long-term objective is to develop this into a modular personal intelligence system capable of local speech processing, memory, reasoning, workflows, and agent-based interaction.


## 2. Problem

Traditional voice assistants and AI services often require cloud infrastructure and provide limited personalization.

Oden explores a different approach:

> Build a personal AI system whose data, models, workflows, and learning process remain under the user's control.

The system should become increasingly useful through normal daily usage rather than requiring a large manually constructed dataset from the beginning.

## 3. Vision

Oden should function as a combination of:

- Personal voice journal
- Personal memory system
- Local AI assistant
- Workflow engine
- Personalized STT system
- Multi-agent platform

The system should gradually evolve from simple voice capture into a broader personal intelligence platform.

## 4. Personal Learning Loop

A central concept is the continuous feedback loop between usage and model improvement.

```text
Speak
  ↓
STT
  ↓
Transcription
  ↓
Correction
  ↓
Training Dataset
  ↓
Model Training
  ↓
New Model Version
  ↓
STT
```

Corrections made during normal use can become training data for future model versions.

This creates the possibility of gradually adapting Oden to:

- Personal pronunciation
- Speech patterns
- Swedish language usage
- English technical terminology
- Programming terminology
- Personal vocabulary
- Common phrases and expressions


## 5. Agents

Oden should support multiple agents/personas using the same underlying infrastructure.

### Bettan

A general-purpose personal assistant focused on everyday interaction, notes, reminders, and personal information.

### Kaj

A technically oriented assistant focused on programming, software development, and technical reasoning.

### Albert

An analytical assistant focused on research, synthesis, and structured reasoning.

These should be treated as configurable personas/agents rather than completely separate AI systems.

Their voices, personalities, prompts, models, and available tools should be configurable independently from Oden's core infrastructure.

## 6. Long-Term Direction

The long-term direction includes investigating whether a smaller STT model can eventually be trained or heavily adapted specifically for:

- A single speaker
- Swedish
- Technical vocabulary
- Personal speech patterns
- Low-latency local inference

This is an exploration rather than a current implementation requirement.


## 7. Philosophy

Oden should be a tool that listens, remembers, learns, and helps while keeping the user's data under the user's control.

The system should prioritize useful infrastructure and measurable progress over premature autonomy.

---


[← Back to README](../README.md)