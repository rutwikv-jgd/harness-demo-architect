import React from 'react'

function App() {
  return (
    <div className="min-h-screen bg-harness-dark text-white">
      <header className="border-b border-white/10 px-6 py-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-harness-blue rounded-lg flex items-center justify-center font-bold text-sm">DA</div>
            <h1 className="text-xl font-semibold tracking-tight" style={{fontFamily: 'Space Grotesk'}}>
              Demo Architect
            </h1>
            <span className="text-xs bg-harness-blue/20 text-harness-teal px-2 py-0.5 rounded-full">
              AI-Powered
            </span>
          </div>
          <span className="text-sm text-white/40">Harness SE Copilot</span>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-6 py-12">
        <p className="text-white/60 text-center text-lg">
          Loading Demo Architect...
        </p>
        <p className="text-white/40 text-center text-sm mt-2">
          Full UI coming in the next build step
        </p>
      </main>
    </div>
  )
}

export default App
