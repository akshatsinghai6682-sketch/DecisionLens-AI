import React from 'react';
import { AlertCircle } from 'lucide-react';

export const Disclaimer: React.FC = () => {
  return (
    <div className="bg-amber-50 border border-amber-200 rounded-lg p-4 my-4 flex gap-3">
      <AlertCircle className="text-amber-600 flex-shrink-0 mt-0.5" size={20} />
      <div className="text-sm text-amber-800">
        <p className="font-semibold mb-1">Important: This is a Decision Aid, Not a Decision</p>
        <p>
          DecisionLens AI provides analysis and perspectives to help you think through decisions.
          It does not make decisions for you. You are responsible for your final choice.
        </p>
        <p className="mt-2">
          The AI shows confidence levels and uncertainty. Trust your judgment, gather additional
          information as needed, and make decisions aligned with your values.
        </p>
      </div>
    </div>
  );
};
