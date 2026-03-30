import React from 'react'
import { Search, Layout, Swords, FileText, CheckCircle2, Loader2, AlertCircle } from 'lucide-react'

const AGENT_ICONS = {
  'Research Agent': Search,
  'Demo Architect': Layout,
  'Compete Agent': Swords,
  'Content Agent': FileText,
}

const AGENT_DESCRIPTIONS = {
  'Research Agent': 'Analyzing prospect profile, mapping industry pain points, identifying relevant customer stories...',
  'Demo Architect': 'Building tailored demo script, sequencing modules, crafting talk track and competitive traps...',
  'Compete Agent': 'Generating battle cards, identifying competitor weaknesses, preparing evaluation criteria...',
  'Content Agent': 'Creating slide deck content, formatting leave-behind document, drafting follow-up email...',
}

const AGENT_COLORS = {
  'Research Agent': { bg: 'bg-teal-500/10', border: 'border-teal-500/20', text: 'text-teal-400', glow: 'shadow-teal-500/10' },
  'Demo Architect': { bg: 'bg-orange-500/10', border: 'border-orange-500/20', text: 'text-orange-400', glow: 'shadow-orange-500/10' },
  'Compete Agent': { bg: 'bg-amber-500/10', border: 'border-amber-500/20', text: 'text-amber-400', glow: 'shadow-amber-500/10' },
  'Content Agent': { bg: 'bg-blue-500/10', border: 'border-blue-500/20', text: 'text-blue-400', glow: 'shadow-blue-500/10' },
}

export default function AgentProgress({ agents, error, onRetry, dealData }) {
  const allComplete = agents.length > 0 && agents.every(a => a.status === 'complete')
  const hasError = agents.some(a => a.status === 'error')

  return (
    <div className="max-w-2xl mx-auto">
      {/* Header */}
      <div className="text-center mb-10">
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/20 mb-4">
          {!allComplete && !hasError && <Loader2 size={12} className="text-blue-400 animate-spin" />}
          {allComplete && <CheckCircle2 size={12} className="text-emerald-400" />}
          {hasError && <AlertCircle size={12} className="text-red-400" />}
          <span className="text-[11px] text-blue-400">
            {hasError ? 'Error occurred' : allComplete ? 'All agents complete' : 'AI agents working...'}
          </span>
        </div>
        <h2 className="text-2xl font-bold text-white mb-2" style={{ fontFamily: 'Space Grotesk, sans-serif' }}>
          {hasError ? 'Something went wrong' : allComplete ? 'Assembling your deliverables' : 'Agents are preparing your demo'}
        </h2>
        <p className="text-sm text-white/30">
          {dealData?.company_name} — {dealData?.industry}
        </p>
      </div>

      {/* Agent Cards */}
      <div className="space-y-3">
        {agents.map((agent, idx) => {
          const Icon = AGENT_ICONS[agent.name] || FileText
          const colors = AGENT_COLORS[agent.name] || AGENT_COLORS['Research Agent']
          const desc = AGENT_DESCRIPTIONS[agent.name] || 'Processing...'

          return (
            <div
              key={agent.name}
              className={`p-4 rounded-xl border transition-all duration-500 ${
                agent.status === 'running'
                  ? `${colors.bg} ${colors.border} shadow-lg ${colors.glow}`
                  : agent.status === 'complete'
                  ? 'bg-emerald-500/5 border-emerald-500/15'
                  : agent.status === 'error'
                  ? 'bg-red-500/5 border-red-500/15'
                  : 'bg-white/[0.02] border-white/[0.05]'
              }`}
              style={{
                animation: agent.status === 'running' ? 'fadeIn 0.5s ease-out' : undefined,
              }}
            >
              <div className="flex items-start gap-3">
                {/* Icon */}
                <div className={`w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 ${
                  agent.status === 'running' ? colors.bg : 
                  agent.status === 'complete' ? 'bg-emerald-500/10' :
                  'bg-white/[0.03]'
                }`}>
                  {agent.status === 'running' ? (
                    <Loader2 size={16} className={`${colors.text} animate-spin`} />
                  ) : agent.status === 'complete' ? (
                    <CheckCircle2 size={16} className="text-emerald-400" />
                  ) : agent.status === 'error' ? (
                    <AlertCircle size={16} className="text-red-400" />
                  ) : (
                    <Icon size={16} className="text-white/20" />
                  )}
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between">
                    <h3 className={`text-sm font-medium ${
                      agent.status === 'running' ? 'text-white' :
                      agent.status === 'complete' ? 'text-emerald-300/80' :
                      'text-white/50'
                    }`}>
                      {agent.name}
                    </h3>
                    <span className={`text-[10px] uppercase tracking-wider ${
                      agent.status === 'running' ? colors.text :
                      agent.status === 'complete' ? 'text-emerald-400/60' :
                      agent.status === 'error' ? 'text-red-400/60' :
                      'text-white/20'
                    }`}>
                      {agent.status === 'running' ? 'Processing' :
                       agent.status === 'complete' ? 'Complete' :
                       agent.status === 'error' ? 'Failed' : 'Waiting'}
                    </span>
                  </div>
                  {agent.status === 'running' && (
                    <p className="text-[12px] text-white/30 mt-1 leading-relaxed">{desc}</p>
                  )}
                  {agent.status === 'running' && (
                    <div className="mt-2.5 h-1 rounded-full bg-white/[0.05] overflow-hidden">
                      <div className="h-full rounded-full bg-gradient-to-r from-blue-500/50 to-cyan-400/50 animate-progress" />
                    </div>
                  )}
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Error retry button */}
      {hasError && error && (
        <div className="mt-6 text-center">
          <p className="text-sm text-red-400/70 mb-3">{error}</p>
          <button
            onClick={onRetry}
            className="px-4 py-2 rounded-lg bg-white/[0.05] border border-white/[0.1] text-sm text-white/60 hover:text-white hover:bg-white/[0.08] transition-all"
          >
            Retry
          </button>
        </div>
      )}

      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(8px); }
          to { opacity: 1; transform: translateY(0); }
        }
        @keyframes progress {
          0% { width: 0%; }
          50% { width: 70%; }
          100% { width: 100%; }
        }
        .animate-progress {
          animation: progress 8s ease-out forwards;
        }
      `}</style>
    </div>
  )
}
