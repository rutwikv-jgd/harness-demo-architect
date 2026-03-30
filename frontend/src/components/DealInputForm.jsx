import React, { useState } from 'react'
import { ChevronRight, Building2, Users, Wrench, Target, Swords, Send } from 'lucide-react'

const INDUSTRY_OPTIONS = [
  'Financial Services', 'Retail & E-Commerce', 'Travel & Hospitality',
  'Technology / SaaS', 'Healthcare & Life Sciences', 'Energy & Utilities',
  'Media & Entertainment', 'Manufacturing', 'Telecommunications', 'Government / Public Sector',
]

export default function DealInputForm({ onSubmit, stages }) {
  const [stage, setStage] = useState('demo_prep')
  const [form, setForm] = useState({
    company_name: '',
    industry: '',
    employee_count: '',
    engineering_team_size: '',
    sales_stage: 'demo_prep',
    deal_size_estimate: '',
    timeline: '',
    current_tools: '',
    cloud_providers: '',
    tech_stack: '',
    deployment_frequency: '',
    pain_points: '',
    key_requirements: '',
    compliance_needs: '',
    competitors_in_deal: '',
    incumbent_tools: '',
    primary_buyer_persona: '',
    technical_evaluators: '',
    champion: '',
    output_format: 'both',
  })

  const update = (field, value) => {
    setForm(prev => ({ ...prev, [field]: value }))
    if (field === 'sales_stage') setStage(value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit({ ...form, sales_stage: stage })
  }

  const isReady = form.company_name && form.industry

  return (
    <div className="max-w-3xl mx-auto">
      {/* Hero */}
      <div className="text-center mb-10">
        <h2
          className="text-3xl font-bold text-white mb-3 tracking-tight"
          style={{ fontFamily: 'Space Grotesk, sans-serif' }}
        >
          Prepare your next Harness demo
        </h2>
        <p className="text-white/40 text-sm max-w-lg mx-auto">
          Enter your deal context below. Our AI agents will generate a tailored demo script,
          competitive battle cards, and customer-ready deliverables.
        </p>
      </div>

      {/* Stage Selector */}
      <div className="mb-8">
        <label className="block text-[11px] text-white/30 uppercase tracking-wider mb-3">Sales stage</label>
        <div className="grid grid-cols-5 gap-2">
          {stages.map((s) => (
            <button
              key={s.id}
              type="button"
              onClick={() => update('sales_stage', s.id)}
              className={`py-2.5 px-3 rounded-lg text-xs font-medium transition-all border ${
                stage === s.id
                  ? 'bg-blue-500/15 border-blue-500/40 text-blue-400'
                  : 'bg-white/[0.02] border-white/[0.06] text-white/40 hover:border-white/10 hover:text-white/60'
              }`}
            >
              <span className="block text-[10px] text-white/20 mb-0.5">{s.icon}</span>
              {s.label}
            </button>
          ))}
        </div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Company Info Section */}
        <FormSection icon={<Building2 size={14} />} title="Company information">
          <div className="grid grid-cols-2 gap-4">
            <Input
              label="Company name *"
              value={form.company_name}
              onChange={v => update('company_name', v)}
              placeholder="e.g. Acme Financial"
            />
            <Select
              label="Industry *"
              value={form.industry}
              onChange={v => update('industry', v)}
              options={INDUSTRY_OPTIONS}
              placeholder="Select industry"
            />
          </div>
          <div className="grid grid-cols-3 gap-4">
            <Input
              label="Employee count"
              value={form.employee_count}
              onChange={v => update('employee_count', v)}
              placeholder="e.g. 5,000"
            />
            <Input
              label="Engineering team size"
              value={form.engineering_team_size}
              onChange={v => update('engineering_team_size', v)}
              placeholder="e.g. 200 developers"
            />
            <Input
              label="Deal size estimate"
              value={form.deal_size_estimate}
              onChange={v => update('deal_size_estimate', v)}
              placeholder="e.g. $250K ACV"
            />
          </div>
        </FormSection>

        {/* Technical Context — shown for discovery and beyond */}
        {['discovery', 'demo_prep', 'poc', 'expansion'].includes(stage) && (
          <FormSection icon={<Wrench size={14} />} title="Technical context">
            <div className="grid grid-cols-2 gap-4">
              <Input
                label="Current CI/CD tools"
                value={form.current_tools}
                onChange={v => update('current_tools', v)}
                placeholder="e.g. Jenkins, GitHub Actions, ArgoCD"
              />
              <Input
                label="Cloud providers"
                value={form.cloud_providers}
                onChange={v => update('cloud_providers', v)}
                placeholder="e.g. AWS, Azure, GCP"
              />
            </div>
            <div className="grid grid-cols-2 gap-4">
              <Input
                label="Tech stack"
                value={form.tech_stack}
                onChange={v => update('tech_stack', v)}
                placeholder="e.g. Kubernetes, Docker, Terraform"
              />
              <Input
                label="Deployment frequency"
                value={form.deployment_frequency}
                onChange={v => update('deployment_frequency', v)}
                placeholder="e.g. Weekly, Monthly, Ad-hoc"
              />
            </div>
          </FormSection>
        )}

        {/* Pain Points — shown for demo_prep and beyond */}
        {['demo_prep', 'poc', 'expansion'].includes(stage) && (
          <FormSection icon={<Target size={14} />} title="Pain points & requirements">
            <TextArea
              label="Pain points discovered"
              value={form.pain_points}
              onChange={v => update('pain_points', v)}
              placeholder="e.g. Deployments take 3 hours, no rollback automation, Jenkins maintenance consuming 2 FTEs, security scanning blocks releases for days..."
              rows={3}
            />
            <div className="grid grid-cols-2 gap-4">
              <TextArea
                label="Key requirements"
                value={form.key_requirements}
                onChange={v => update('key_requirements', v)}
                placeholder="e.g. Must support Kubernetes, need SOC2 compliance, require RBAC..."
                rows={2}
              />
              <TextArea
                label="Compliance needs"
                value={form.compliance_needs}
                onChange={v => update('compliance_needs', v)}
                placeholder="e.g. SOX, PCI-DSS, HIPAA, FedRAMP..."
                rows={2}
              />
            </div>
          </FormSection>
        )}

        {/* Competitive — shown for demo_prep and poc */}
        {['demo_prep', 'poc'].includes(stage) && (
          <FormSection icon={<Swords size={14} />} title="Competitive landscape">
            <div className="grid grid-cols-2 gap-4">
              <Input
                label="Competitors in this deal"
                value={form.competitors_in_deal}
                onChange={v => update('competitors_in_deal', v)}
                placeholder="e.g. GitLab, GitHub Actions"
              />
              <Input
                label="Incumbent tools to displace"
                value={form.incumbent_tools}
                onChange={v => update('incumbent_tools', v)}
                placeholder="e.g. Jenkins (5 years), Spinnaker"
              />
            </div>
          </FormSection>
        )}

        {/* Stakeholders — shown for discovery and beyond */}
        {['discovery', 'demo_prep', 'poc', 'expansion'].includes(stage) && (
          <FormSection icon={<Users size={14} />} title="Stakeholders">
            <div className="grid grid-cols-3 gap-4">
              <Input
                label="Primary buyer persona"
                value={form.primary_buyer_persona}
                onChange={v => update('primary_buyer_persona', v)}
                placeholder="e.g. VP of Engineering"
              />
              <Input
                label="Technical evaluators"
                value={form.technical_evaluators}
                onChange={v => update('technical_evaluators', v)}
                placeholder="e.g. DevOps Lead, Platform Team"
              />
              <Input
                label="Champion"
                value={form.champion}
                onChange={v => update('champion', v)}
                placeholder="e.g. Director of Platform Eng"
              />
            </div>
          </FormSection>
        )}

        {/* Output Format */}
        <div className="flex items-center gap-4 pt-2">
          <label className="text-[11px] text-white/30 uppercase tracking-wider">Output</label>
          {['document', 'slides', 'both'].map(fmt => (
            <button
              key={fmt}
              type="button"
              onClick={() => update('output_format', fmt)}
              className={`px-3 py-1.5 rounded-md text-xs border transition-all ${
                form.output_format === fmt
                  ? 'bg-blue-500/15 border-blue-500/40 text-blue-400'
                  : 'bg-white/[0.02] border-white/[0.06] text-white/30 hover:text-white/50'
              }`}
            >
              {fmt === 'both' ? 'Document + Slides' : fmt.charAt(0).toUpperCase() + fmt.slice(1)}
            </button>
          ))}
        </div>

        {/* Submit */}
        <button
          type="submit"
          disabled={!isReady}
          className={`w-full py-3.5 rounded-xl text-sm font-semibold flex items-center justify-center gap-2 transition-all ${
            isReady
              ? 'bg-gradient-to-r from-blue-500 to-cyan-400 text-white hover:opacity-90 shadow-lg shadow-blue-500/20'
              : 'bg-white/[0.04] text-white/20 cursor-not-allowed'
          }`}
        >
          <Send size={14} />
          Generate with AI Agents
          <ChevronRight size={14} />
        </button>
      </form>

      {/* Example Scenario */}
      <div className="mt-8 p-4 rounded-xl bg-white/[0.02] border border-white/[0.04]">
        <div className="flex items-center justify-between mb-2">
          <span className="text-[11px] text-white/25 uppercase tracking-wider">Quick fill — example scenario</span>
          <button
            onClick={() => {
              setStage('demo_prep')
              setForm({
                company_name: 'National Federal Bank',
                industry: 'Financial Services',
                employee_count: '15,000',
                engineering_team_size: '400 developers',
                sales_stage: 'demo_prep',
                deal_size_estimate: '$350K ACV',
                timeline: '90 days',
                current_tools: 'Jenkins, Spinnaker, SonarQube, Artifactory',
                cloud_providers: 'AWS (primary), Azure (secondary)',
                tech_stack: 'Kubernetes, Docker, Terraform, Java, Python microservices',
                deployment_frequency: 'Bi-weekly with 3-day deployment windows',
                pain_points: 'Jenkins maintenance consuming 4 FTEs. Deployments take 6 hours with manual approvals. No automated rollback — last production incident took 8 hours to remediate. Security scanning adds 2 days to every release. Cloud costs grew 40% YoY with no visibility into waste.',
                key_requirements: 'Must support multi-region AWS deployments, need SOX and PCI-DSS compliance, require RBAC with SSO integration, must integrate with ServiceNow for change management',
                compliance_needs: 'SOX, PCI-DSS, OCC regulatory requirements',
                competitors_in_deal: 'GitLab Ultimate (primary competitor), also evaluating GitHub Enterprise',
                incumbent_tools: 'Jenkins (7 years), Spinnaker (3 years)',
                primary_buyer_persona: 'VP of Engineering',
                technical_evaluators: 'DevOps Platform Team Lead, Sr. Cloud Architect, InfoSec Director',
                champion: 'Director of Platform Engineering — frustrated with Jenkins maintenance',
                output_format: 'both',
              })
            }}
            className="text-[11px] text-blue-400/60 hover:text-blue-400 transition-colors cursor-pointer"
          >
            Load example →
          </button>
        </div>
        <p className="text-[11px] text-white/20">
          National Federal Bank — 400 dev financial services company evaluating Harness against GitLab for CI/CD modernization with security and cost management needs.
        </p>
      </div>
    </div>
  )
}

// ---- Reusable Form Components ----

function FormSection({ icon, title, children }) {
  return (
    <div className="p-5 rounded-xl bg-white/[0.02] border border-white/[0.05] space-y-4">
      <div className="flex items-center gap-2 mb-1">
        <span className="text-white/20">{icon}</span>
        <h3 className="text-xs font-medium text-white/40 uppercase tracking-wider">{title}</h3>
      </div>
      {children}
    </div>
  )
}

function Input({ label, value, onChange, placeholder }) {
  return (
    <div>
      <label className="block text-[11px] text-white/25 mb-1.5">{label}</label>
      <input
        type="text"
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder={placeholder}
        className="w-full bg-white/[0.03] border border-white/[0.06] rounded-lg px-3 py-2 text-sm text-white placeholder-white/15 focus:outline-none focus:border-blue-500/40 focus:bg-white/[0.04] transition-all"
      />
    </div>
  )
}

function Select({ label, value, onChange, options, placeholder }) {
  return (
    <div>
      <label className="block text-[11px] text-white/25 mb-1.5">{label}</label>
      <select
        value={value}
        onChange={e => onChange(e.target.value)}
        className="w-full bg-white/[0.03] border border-white/[0.06] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-blue-500/40 transition-all appearance-none"
      >
        <option value="" className="bg-[#1a1f2e]">{placeholder}</option>
        {options.map(opt => (
          <option key={opt} value={opt} className="bg-[#1a1f2e]">{opt}</option>
        ))}
      </select>
    </div>
  )
}

function TextArea({ label, value, onChange, placeholder, rows = 2 }) {
  return (
    <div>
      <label className="block text-[11px] text-white/25 mb-1.5">{label}</label>
      <textarea
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder={placeholder}
        rows={rows}
        className="w-full bg-white/[0.03] border border-white/[0.06] rounded-lg px-3 py-2 text-sm text-white placeholder-white/15 focus:outline-none focus:border-blue-500/40 focus:bg-white/[0.04] transition-all resize-none"
      />
    </div>
  )
}
