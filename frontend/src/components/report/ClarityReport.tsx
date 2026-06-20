import React from 'react';
import { Download, Share2 } from 'lucide-react';

interface ClarityReportProps {
  decisionTitle: string;
  keyInsights: string[];
  rankedPriorities: string[];
  coreTradeoffs: string[];
  missingInformation: string[];
  nextResearchSteps: string[];
  decisionFramework: string;
  gutCheckQuestions: string[];
  onExportPDF: () => void;
}

export const ClarityReport: React.FC<ClarityReportProps> = ({
  decisionTitle,
  keyInsights,
  rankedPriorities,
  coreTradeoffs,
  missingInformation,
  nextResearchSteps,
  decisionFramework,
  gutCheckQuestions,
  onExportPDF,
}) => {
  return (
    <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-lg p-8 space-y-6">
      <div className="text-center border-b pb-6">
        <h1 className="text-3xl font-bold text-gray-900">{decisionTitle}</h1>
        <p className="text-gray-600 mt-2">DecisionLens AI Clarity Report</p>
      </div>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Key Insights</h2>
        <ul className="space-y-2">
          {keyInsights.map((insight, idx) => (
            <li key={idx} className="flex gap-2 text-gray-700">
              <span className="text-blue-600 font-bold">•</span>
              <span>{insight}</span>
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Ranked Priorities</h2>
        <ol className="space-y-2 list-decimal list-inside">
          {rankedPriorities.map((priority, idx) => (
            <li key={idx} className="text-gray-700">{priority}</li>
          ))}
        </ol>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Core Tradeoffs</h2>
        <ul className="space-y-2">
          {coreTradeoffs.map((tradeoff, idx) => (
            <li key={idx} className="p-3 bg-amber-50 rounded border border-amber-200 text-gray-700">
              {tradeoff}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Missing Information</h2>
        <ul className="space-y-2">
          {missingInformation.map((info, idx) => (
            <li key={idx} className="flex gap-2 text-gray-700">
              <span className="text-red-600 font-bold">!</span>
              <span>{info}</span>
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Next Research Steps</h2>
        <ol className="space-y-2">
          {nextResearchSteps.map((step, idx) => (
            <li key={idx} className="p-3 bg-blue-50 rounded text-gray-700">
              <span className="font-semibold">{idx + 1}. </span>{step}
            </li>
          ))}
        </ol>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Decision Framework</h2>
        <div className="p-4 bg-green-50 rounded border border-green-200 text-gray-700">
          {decisionFramework}
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Gut Check Questions</h2>
        <ul className="space-y-2">
          {gutCheckQuestions.map((question, idx) => (
            <li key={idx} className="flex gap-2 text-gray-700">
              <span className="text-purple-600 font-bold">?</span>
              <span className="italic">{question}</span>
            </li>
          ))}
        </ul>
      </section>

      <div className="flex gap-4 pt-6 border-t">
        <button
          onClick={onExportPDF}
          className="flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 font-semibold"
        >
          <Download size={20} />
          Export as PDF
        </button>
        <button className="flex items-center gap-2 bg-gray-200 text-gray-900 px-6 py-3 rounded-lg hover:bg-gray-300 font-semibold">
          <Share2 size={20} />
          Share
        </button>
      </div>
    </div>
  );
};
