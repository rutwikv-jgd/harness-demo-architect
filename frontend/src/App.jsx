import React, { useState } from 'react'
import DealInputForm from './components/DealInputForm'
import AgentProgress from './components/AgentProgress'
import OutputDisplay from './components/OutputDisplay'
import { Zap, RotateCcw } from 'lucide-react'

const STAGES = [
  { id: 'pre_discovery', label: 'Pre-Discovery', icon: '1' },
  { id: 'discovery', label: 'Discovery', icon: '2' },
  { id: 'demo_prep', label: 'Demo Prep', icon: '3' },
  { id: 'poc', label: 'POC', icon: '4' },
  { id: 'expansion', label: 'Expansion', icon: '5' },
]

function App() {
  const [currentView, setCurrentView] = useState('input') // input | processing | results
  const [dealData, setDealData] = useState(null)
  const [result, setResult] = useState(null)
  const [agentStatuses, setAgentStatuses] = useState([])
  const [error, setError] = useState(null)

  const handleSubmit = async (formData) => {
    setDealData(formData)
    setCurrentView('processing')
    setError(null)
    setAgentStatuses([])

    // Simulate agent status updates for visual effect
    const stage = formData.sales_stage
    const agents = getAgentsForStage(stage)

    // Show agents starting one by one
    for (let i = 0; i < agents.length; i++) {
      setAgentStatuses(prev => [...prev, { name: agents[i].name, status: 'running', icon: agents[i].icon }])
      if (i < agents.length - 1) {
        await sleep(800)
      }
    }

    try {
      const API_URL = import.meta.env.VITE_API_URL || ''
      const response = await fetch(`${API_URL}/api/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      })

      if (!response.ok) throw new Error(`API error: ${response.status}`)

      const data = await response.json()
      setResult(data)

      // Mark all agents as complete
      setAgentStatuses(prev => prev.map(a => ({ ...a, status: 'complete' })))
      await sleep(1000)
      setCurrentView('results')
    } catch (err) {
      setError(err.message)
      setAgentStatuses(prev => prev.map(a => ({ ...a, status: 'error' })))
    }
  }

  const handleReset = () => {
    setCurrentView('input')
    setDealData(null)
    setResult(null)
    setAgentStatuses([])
    setError(null)
  }

  return (
    <div className="min-h-screen bg-[#0a0f1a]">
      {/* Header */}
      <header className="border-b border-white/[0.06] bg-[#0d1321]/80 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-blue-500 to-cyan-400 flex items-center justify-center">
              <Zap size={18} className="text-white" />
            </div>
            <div>
              <h1 className="text-[15px] font-semibold text-white tracking-tight" style={{ fontFamily: 'Space Grotesk, sans-serif' }}>
                Demo Architect
              </h1>
              <p className="text-[10px] text-white/30 tracking-widest uppercase">Harness SE Copilot</p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            {currentView !== 'input' && (
              <button
                onClick={handleReset}
                className="flex items-center gap-1.5 text-xs text-white/40 hover:text-white/70 transition-colors"
              >
                <RotateCcw size={12} />
                New deal
              </button>
            )}
            <div className="flex items-center gap-1.5">
              <div className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              <span className="text-[11px] text-white/30">AI agents online</span>
            </div>
          </div>
        </div>
      </header>

      {/* Stage Indicator */}
      {currentView !== 'input' && dealData && (
        <div className="bg-[#0d1321]/60 border-b border-white/[0.04]">
          <div className="max-w-6xl mx-auto px-6 py-2 flex items-center gap-6">
            <span className="text-[11px] text-white/25 uppercase tracking-wider">Stage</span>
            <div className="flex gap-1">
              {STAGES.map((stage) => (
                <div
                  key={stage.id}
                  className={`px-3 py-1 rounded-full text-[11px] transition-all ${
                    dealData.sales_stage === stage.id
                      ? 'bg-blue-500/20 text-blue-400 border border-blue-500/30'
                      : 'text-white/20'
                  }`}
                >
                  {stage.label}
                </div>
              ))}
            </div>
            <span className="ml-auto text-[11px] text-white/25">{dealData.company_name}</span>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-6 py-8">
        {currentView === 'input' && (
          <DealInputForm onSubmit={handleSubmit} stages={STAGES} />
        )}

        {currentView === 'processing' && (
          <AgentProgress
            agents={agentStatuses}
            error={error}
            onRetry={() => handleSubmit(dealData)}
            dealData={dealData}
          />
        )}

        {currentView === 'results' && result && (
          <OutputDisplay result={result} dealData={dealData} onReset={handleReset} />
        )}
      </main>
    </div>
  )
}

function getAgentsForStage(stage) {
  const agents = {
    pre_discovery: [
      { name: 'Research Agent', icon: 'search' },
    ],
    discovery: [
      { name: 'Research Agent', icon: 'search' },
      { name: 'Demo Architect', icon: 'layout' },
    ],
    demo_prep: [
      { name: 'Research Agent', icon: 'search' },
      { name: 'Demo Architect', icon: 'layout' },
      { name: 'Compete Agent', icon: 'swords' },
      { name: 'Content Agent', icon: 'file' },
    ],
    poc: [
      { name: 'Research Agent', icon: 'search' },
      { name: 'Demo Architect', icon: 'layout' },
    ],
    expansion: [
      { name: 'Research Agent', icon: 'search' },
      { name: 'Demo Architect', icon: 'layout' },
    ],
  }
  return agents[stage] || agents.demo_prep
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

export default App
